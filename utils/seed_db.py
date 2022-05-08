from db import db_session
from models import Event, Device
from time import sleep

d1 = Device(name='Seed Cards', location='Kitchen')
d2 = Device(name='Basil', location='Office')
d3 = Device(name='Dill', location='Office')
d4 = Device(name='Chives', location='Office')
d5 = Device(name='Succulents', location='Living Room')

db_session.add(d1)
db_session.add(d2)
db_session.add(d3)
db_session.add(d4)
db_session.add(d5)

db_session.commit()

e10 = Event(deviceID=1, state=0)
e11 = Event(deviceID=1, state=0)
e12 = Event(deviceID=1, state=1)
e13 = Event(deviceID=1, state=2)
e14 = Event(deviceID=1, state=2)

e20 = Event(deviceID=2, state=1)
e21 = Event(deviceID=2, state=2)
e22 = Event(deviceID=2, state=2)
e23 = Event(deviceID=2, state=2)
e24 = Event(deviceID=2, state=2)

e30 = Event(deviceID=3, state=0)
e31 = Event(deviceID=3, state=0)
e32 = Event(deviceID=3, state=0)
e33 = Event(deviceID=3, state=0)
e34 = Event(deviceID=3, state=0)

e40 = Event(deviceID=4, state=0)
e41 = Event(deviceID=4, state=0)
e42 = Event(deviceID=4, state=0)
e43 = Event(deviceID=4, state=0)
e44 = Event(deviceID=4, state=1)

e50 = Event(deviceID=5, state=0)
e51 = Event(deviceID=5, state=0)
e52 = Event(deviceID=5, state=0)
e53 = Event(deviceID=5, state=1)
e54 = Event(deviceID=5, state=2)

allEvents = [
    e10, e11, e12, e13, e14, 
    e20, e21, e22, e23, e24, 
    e30, e31, e32, e33, e34, 
    e40, e41, e42, e43, e44, 
    e50, e51, e52, e53, e54
]

for event in allEvents:
    print(event)
    db_session.add(event)
    db_session.commit()
    sleep(2)