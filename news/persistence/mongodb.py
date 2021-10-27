import os
import pymongo

from typing import Any, Dict, List

from news.models.Headline import Headline
from news.values.db import (NEWS_DATABASE, HEADLINES_COLLECTION)


# client = pymongo.MongoClient(
#     host=os.getenv('MONGO_HOST'),
#     port=int(os.getenv('MONGO_LOCAL_PORT')),
#     username=os.getenv('MONGO_USERNAME'),
#     password=os.getenv('MONGO_PASSWORD'),
#     authSource='admin'
# )

def insert_headlines(headlines: List[Dict[str, Any]]) -> None:
    # TODO: headline.to_json
    # TODO: research performance of insert one vs insert many
    # client[NEWS_DATABASE][HEADLINES_COLLECTION].insert_many(headlines)
    pass
