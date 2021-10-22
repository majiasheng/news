from typing import Any, Dict

from news.api_key import API_KEY
from newsapi import NewsApiClient
from news.values import category
from news.values import country

newsapi = NewsApiClient(api_key=API_KEY)

def fetch_all_headlines(country: str=country.US) -> Dict[str, Any]:
    for cat in category.all:
        headlines = newsapi.get_top_headlines(
            category=cat,
            country=country
        )
        # save headlines to db


def get_top_general_headlines(country: str=country.US) -> Dict[str, Any]:
    top_general_headlines = newsapi.get_top_headlines(
        category=category.GENERAL,
        country=country
    )

    return top_general_headlines
