import pymongo

connection_str = 'mongodb://localhost:27017'
client = pymongo.MongoClient(connection_str)


record = {
    "sensor_name": "Sensor 1",
    "PM 25": "123",
    "PM 10": "456" 
}

def connect_to_db():
    pass

def write_record(record):
    db = client.ajtest
    db.test_collection.insert_one(record)

def get_record():
    pass

write_record(record)