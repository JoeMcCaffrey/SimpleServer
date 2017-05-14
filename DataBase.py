import json

class DataBase:

    def __init__(self, dataFile):
        self.__dataFile = dataFile


    def contains(self, key):
        with open(self.__dataFile) as file:
            data = json.load(file)
        #search for matching dict
        for m in data["map"]:
            if m == key:
                return True
            else:
                return False

# insert into map list
    def insert(self, key):
        data = {}
        print 'hello'+ key
        with open(self.__dataFile) as file:
            data = {}
            data = json.load(file)
        print data
        #jsonDict = {}
        jsonDict= key.replace("'", "\"")
        d = json.loads(jsonDict)

        data["map"].append(d)
        print data
        with open(self.__dataFile, 'w') as file:
            json.dump(data, file)

# delete dict from list
    def delete(self, key):
        m = {}
        with open(self.__dataFile) as file:
            data = json.load(file)
        for m in data["map"]:
            print m.keys()
            print key
            if m.keys()[0] == key:
                data["map"].remove(m)
        with open(self.__dataFile, 'w') as file:
            json.dump(data, file)

# update matching keys
    def update(self, key):
        m = {}
        with open(self.__dataFile) as file:
            data = json.load(file)
        for m in data["map"]:
            if m.keys() == key.keys():
                m.update(key)
        with open(self.__dataFile, 'w') as file:
            json.dump(data, file)

# print out the db
    def output(self):
        with open(self.__dataFile) as file:
            data = json.load(file)
        print data

# search for key in db and return it
    def get(self, key):
        json1 ={}
        with open(self.__dataFile) as file:
            data = json.load(file)
            #json1[key] = data[key]
            for m in data["map"]:
                if m == key:
                    return m


    def getSize(self):
        with open(self.__dataFile) as file:
            data = json.load(file)
            return len(data["map"])
