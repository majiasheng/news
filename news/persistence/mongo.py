import os
import pymongo


conn_str = ("mongodb://"
    f"{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}"
    "@"
    f"{os.getenv('MONGO_HOST')}{os.getenv('MONGO_PORT')}"
)

db = pymongo.MongoClient(conn_str)
