import pymongo
import os
from dotenv import load_dotenv
load_dotenv()


# f"mongodb://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_LOCAL_PORT')}"





client = pymongo.MongoClient(
    host=os.getenv('MONGO_HOST'),
    port=int(os.getenv('MONGO_LOCAL_PORT')),
    username=os.getenv('MONGO_USERNAME'),
    password=os.getenv('MONGO_PASSWORD'),
    authSource='admin'
)

import pdb
pdb.set_trace()
for db in client.list_databases():
    print(db)

client.close()
# create collections