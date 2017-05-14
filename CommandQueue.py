
from DataBase import *

class CommandQueue:

    def __init__(self, db):
        self._queue = []
        self._db = db

    def size(self):
        return len(self._queue)


    def enqueue(self, key, command):
        #insert key and command right behind it
        print key
        self._queue.insert(0,key)
        self._queue.insert(0,command)

    def dump(self):
        key = {}
        for i in range(0,len(self._queue)/2):
            key = self._queue.pop()
            print key
            command = self._queue.pop()
            if command == 'update':
                self._db.update(key)
            elif command == 'delete':
                self._db.delete(key)
            elif command == 'new':
                self._db.insert(key)
            else:
                print "error"

    def printQueue(self):
        print self._queue