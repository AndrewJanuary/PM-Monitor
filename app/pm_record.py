from mongoengine import *

class Pm_record():
    sensor_name: StringField(required=True, max_length=256)
    PM_25: StringField(required=True, max_length=20)
    PM_10: StringField(required=True, max_length=20)