from DataBase import *
from flask import *
from CommandQueue import *
import sys

app = Flask(__name__)
app.debug = False

# create database object
db = DataBase('data.json')
commands = CommandQueue(db)

#key lookup
@app.route('/<key>', methods=['GET'])
def retrieve(key):
    if request.method == 'GET':
        if db.contains(key):
            return db.get(key) + "\n"
        else:
            return "404\n"
    else:
        return "404\n"

@app.route('/set', methods=['POST', 'DELETE'])
def route():
    data ={}
    data = request.data
    if request.method == 'POST':
        if(db.lookup(data)):
            commands.enqueue(data, "update")
            return "200\n"
        else:
            commands.enqueue(data, "new")
            return "201\n"

    elif request.method == 'DELETE':
        commands.enqueue(data, "delete")
        return "200\n"

    else:
        return "404\n"

@app.route('/commit', methods=['POST'])
def save():
    if request.method == 'POST' and commands.size() !=0:
        commands.dump()
        return "204\n"
    else:
        return "404\n"

app.run(port= sys.argv[1])