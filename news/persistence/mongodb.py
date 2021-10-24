import os
import pymongo
from news.models.Headlines import Headlines
from values.db import (NEWS_DATABASE, HEADLINES_COLLECTION)

conn_str = ("mongodb://"
    f"{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}"
    "@"
    f"{os.getenv('MONGO_HOST')}{os.getenv('MONGO_PORT')}"
)

client = pymongo.MongoClient(conn_str)

def insert_headlines(headlines: Headlines):
    client[NEWS_DATABASE][HEADLINES_COLLECTION].insert_one(headlines)
