import values

from typing import Any, Dict, List

from news.api_key import API_KEY
from newsapi import NewsApiClient
from news.persistence import mongodb
from news.models.Headlines import Headlines

newsapi = NewsApiClient(api_key=API_KEY)


def get_news_categories() -> List[str]:
    return values.categories.all


def get_news_countries() -> List[str]:
    return values.countries.all


def fetch_and_save_all_headlines(country: str = values.countries.US) -> Dict[str, Any]:
    '''
    Fetch and save all headlines. Use this on every news updates to cache
    results to db. Every subsequent requests to get news should be db calls.
    '''
    for category in values.categories.all:
        headlines = newsapi.get_top_headlines(
            category=category,
            country=country
        )
        # save headlines to db
        mongodb.insert_headlines(
            Headlines(
                country=country, 
            )
        )
