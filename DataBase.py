import json

class DataBase:

    def __init__(self, dataFile):
        self.__dataFile = dataFile

# lookup in db with just key
    def contains(self, key):
        with open(self.__dataFile) as file:
            data = json.load(file)
        #search for matching dict
        for m in data["map"]:
            if m.keys()[0] == key:
                return True
            else:
                return False

# look up with key value pair
    def lookup(self,key):
        with open(self.__dataFile) as file:
            data = json.load(file)
        for m in data["map"]:
            f = json.loads(key)
            if m.keys()[0] == f.keys()[0]:
                return True
            else:
                return False

# insert into map list
    def insert(self, key):
        data = {}
        with open(self.__dataFile) as file:
            data = {}
            data = json.load(file)
        # remove string extras
        jsonDict= key.replace("'", "\"")
        d = json.loads(jsonDict)
        data["map"].append(d)
        with open(self.__dataFile, 'w') as file:
            json.dump(data, file, ensure_ascii = False)

# delete dict from list
    def delete(self, key):
        # open file and find in maps list
        with open(self.__dataFile) as file:
            data = json.load(file)
        for m in data["map"]:
            f = json.loads(key)
            if m.keys()[0] == f:
                data["map"].remove(m)
        with open(self.__dataFile, 'w') as file:
            json.dump(data, file)

# update matching keys
    def update(self, key):
        m = {}
        with open(self.__dataFile) as file:
            data = json.load(file)
        # convert to unicode
        f = json.loads(key)
        for m in data["map"]:
            if m.keys() == f.keys():
                m.update(f)
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
        for m in data["map"]:
            if m.keys()[0] == key:
                return str(m)


    def getSize(self):
        with open(self.__dataFile) as file:
            data = json.load(file)
            return len(data["map"])
