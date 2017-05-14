
from tinydb import TinyDB
from tinydb import Query


class DataBase:


    def __init__(self, dataFile, name):
    # file that will hold the .json database
        self.__db = TinyDB(dataFile)
        self.__db.table(name=name, cache_size =None)
        self.__query = Query()
        self.__table = name

    def insert(self, jsonData):
        self.__db.table(self.__table).insert(jsonData)

    def update(self, jsonData, key):
        self.__db.table(self.__table)

    def get(self, key):
        dick =self.__db.table(self.__table).get(self.__query.name.exists())
        print dick.name

    def contains(self):
        print "hi"


    def remove(key):
        print 'hi'


    def printDB(self):
        print self.__db.all()






