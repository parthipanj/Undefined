def get_db():
    import pymongo
    from generic.config import mongo
    from generic.config import account_id

    client = pymongo.mongo_client.MongoClient(**mongo)

    return client[account_id]
