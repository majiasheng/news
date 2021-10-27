
from typing import Any, Dict, Generator, List

from news.api_key import API_KEY
from newsapi import NewsApiClient
from news.persistence import mongodb
from news.models.Headline import Headline
from . import values

newsapi = NewsApiClient(api_key=API_KEY)


def get_news_categories() -> List[str]:
    return values.categories.ALL


def get_news_countries() -> List[str]:
    return values.countries.ALL


def fetch_headlines(category: str, country: str = values.countries.US) -> Generator[Dict[str, Any], None, None]:
    page = 1
    raw_headlines = newsapi.get_top_headlines(
        category=category,
        country=country,
        page_size=values.common.PAGE_SIZE,
        page=page
    )
    all_raw_headlines = raw_headlines.get('articles', [])

    # page through all articles
    while True:
        page += 1
        if raw_headlines['totalResults'] > values.common.PAGE_SIZE:
            raw_headlines = newsapi.get_top_headlines(
                category=category,
                country=country,
                page_size=values.common.PAGE_SIZE,
                page=page
            )
            all_raw_headlines.extend(raw_headlines.get('articles', []))
        else:
            break
        
    # convert to document
    for headline in all_raw_headlines:
        yield Headline(
            source=headline.get('source'),
            author=headline.get('author'),
            title=headline.get('title'),
            description=headline.get('description'),
            url=headline.get('url'),
            url_to_image=headline.get('urlToImage'),
            published_at=headline.get('publishedAt'),
            content=headline.get('content'),
            country=country,
            category=category
        ).to_json()


def fetch_and_save_all_headlines(country: str = values.countries.US) -> Dict[str, Any]:
    '''
    Fetch and save all headlines. Use this on every news updates to cache
    results to db. Every subsequent requests to get news should be db calls.
    '''
    for category in values.categories.ALL:
        headlines = fetch_headlines(
            category=category,
            country=country
        )

        # batch insert headlines to db
        headline_batch = []
        for headline in headlines:
            import pdb; pdb.set_trace()
            headline_batch.append(headline)
            if len(headline_batch) >= values.common.BATCH_SIZE:
                mongodb.insert_headlines(
                    headline_batch
                )
                # empty batch after insert
                headline_batch = []

        # insert the remaning data
        if len(headline_batch) > 0:
            mongodb.insert_headlines(
                headline_batch
            )
