import pymongo
from werkzeug_ads_app.config import MONGO_DB_CONFIG
from bson.objectid import ObjectId


class MongoDB():

    def __init__(self, MONGO_DB_CONFIG: dict):
        """
        Constructor.
        :param MONGO_DB_CONFIG: (dict)
        :return (new MongoDB obj)
        """
        self._client = pymongo.MongoClient(MONGO_DB_CONFIG['host'], MONGO_DB_CONFIG['port'])
        self._db = self._client[MONGO_DB_CONFIG['name']]
        self._collections = {}
        self.create_collections()

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value: list):
        self._client = value

    @client.deleter
    def client(self):
        del self._client

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, value: list):
        self._db = value

    @db.deleter
    def db(self):
        del self._db

    @property
    def collections(self):
        return self._collections

    @collections.setter
    def collections(self, value: list):
        self._collections = value

    @collections.deleter
    def collections(self):
        del self._collections

    def create_collections(self) -> None:
        """
        Creates and initializes collections of DB.
        :return: (None)
        """
        for collection in MONGO_DB_CONFIG['collections_list']:
            self._collections[collection] = self._db[collection]

    def add_collection(self, collection_name: str) -> None:
        """
        Adds and initializes the collection of DB.
        :param collection_name: (str)
        :return: (None)
        """
        self._collections[collection_name] = self._db[collection_name]

    def get_collection(self, collection_name: str) -> pymongo.cursor.Cursor:
        """
        Gets a cursor of the collection.
        :param collection_name: (str)
        :return: (pymongo.cursor.Cursor obj)
        """
        return self._collections[collection_name]

    def insert_document(self, collection_name: str, document: dict) -> None:
        """
        Inserts document into collection.
        :param collection_name: (str)
        :param document: (dict)
        :return: (None)
        """
        self._collections[collection_name].insert_one(document)

    def get_collection_docs(self, collection_name: str) -> list:
        """
        Gets list of documents of the collection.
        :param collection_name:
        :return: (list)
        """
        return [doc for doc in self._collections[collection_name].find()]

    def get_sorted_collection_docs(self, collection_name: str, reverse_val: bool) -> list:
        """
        Gets sorted list of documents of the collection.
        :param collection_name: (str)
        :param reverse_val: (bool)
        :return: (list)
        """
        ads = [ad for ad in self._collections[collection_name].find()]
        return sorted(ads, key=lambda k: k['created_at'], reverse=reverse_val)

    def delete_one_doc_of_collection(self, collection_name: str, object_id: str) -> None:
        """
        :param collection_name: (str)
        :param object_id: (str)
        :return: (None)
        """
        self._collections[collection_name].delete_one({'_id': ObjectId(object_id)})


    def delete_all_docs_of_collection(self, collection_name: str) -> None:
        """
        :param collection_name: (str)
        :return: (None)
        """
        self._collections[collection_name].delete_many({})


    def drop_collection(self, collection_name: str) -> None:
        """
        :param collection_name: (str)
        :return: (None)
        """
        self._collections[collection_name].drop()
