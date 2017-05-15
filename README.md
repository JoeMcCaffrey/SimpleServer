# Simple Server


This server has 4 main parts: The server script, CommandQueue class, DataBase class and data.json file.

The Http requests are handled by the server script running on port 4000, the script uses the python flask library to take different actions depending on the requested subdomains.

When the Server is started DataBase and CommandQueue objects are created, and the server will start listening.

The subdomain which is neither /set or /commit will index a database using the Database object methods to look up a key in the data.json file, either returning it or 404 if not found.

The database object will read in the json data from the file and preform opertations like: lookup, contains, delete, update and insert.

For subdomains /set or /commit the Http verb is checked and different actions are taken for specific verbs. 

The /set subdomain uses a CommandQueue object to store data and http verbs from the client into a Queue. This continues until the /commit subdomain is called.

The /commit subdomain is called and the CommandQueue will empty the queue taking database actions based on the Http verb and will store, delete or update data into the data.json file.

The server will continue to listen for commands from the client until stopped.

# Dependencies

Python flask:
	pip install flask

Python json:
	the python json library which comes standard.

# Comments

Given more time I would of used a more robust database technology than just read/ writing to a file. 

I would of liked to have designed the Server using more of a OOD approach. Flask was throwing errors when declared inside of a class. More research is needed to get this part working.

A problem I ran into was reading and writing the data from the data.json file was not a string but a unicode type. This led to a type mismatch when trying to do comparisons. My research suggested that this may have been a python version issue since I was using 2.7. With more time I would of redone this in python 3 with hoping this was fixed. 

Python version: Python 2.7.13
Written on Fedora 25 x86
