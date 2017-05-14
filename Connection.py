from DataBase import *


db = DataBase('data.json')



db.insert({'hi':'joe'})
db.insert({'le': 'john'})
#db.update({'hi': 'john'})
print db.getSize()
print db.contains({'le': 'john'})

db.update({'le': 'joe'})

db.delete("le")
print db.getSize()

#db.remove({'hi': 'john'})


