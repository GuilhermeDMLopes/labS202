import pymongo


class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

    def create(self, nome, autor, ano, preco):
        return self.collection.insert_one({"nome": nome, "autor": autor, "ano": ano, "preco": preco})

    def read(self):
        return self.collection.find({})

    def update(self, nome, preco):
        return self.collection.update_one(
            {"nome": nome},
            {
                "$set": {"nome": nome},
                "$set": {"preco": preco},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, nome):
        return self.collection.delete_one({"nome": nome})
