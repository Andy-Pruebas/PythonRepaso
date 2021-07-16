from pymongo import MongoClient
client = MongoClient('localhost')

db=client['PyMongo']
col=db['Productos']

