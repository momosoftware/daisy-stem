from db import db_session
from models import Event, Device
from time import sleep
from datetime import datetime, timedelta
import random
import corpora

# time (in seconds) between events
timeBetweenEvents = 30

def genDevices(numberOfDevices=5):
    deviceIDs = []
    
    for d in range(numberOfDevices):
        room = random.choice(corpora.rooms).title()
        plant = random.choice(corpora.herbs + corpora.spices + corpora.vegetables).title()
        device = Device(name=plant, location=room)
        
        db_session.add(device)
        db_session.commit()
        db_session.refresh(device)

        deviceIDs.append(device.id)
    
    return deviceIDs

def genEvents(deviceIDs, numberOfEvents=50):
    for deviceID in deviceIDs:
        startTime = datetime.now()
        curState = random.randint(0,2) # our initial state
        # generate azditional states that are 1 higher or lower than the current state
        for i in range(numberOfEvents):
            if random.random() < 0.5:
                if curState != 2:
                    curState += 1
            else:
                if curState != 0:
                    curState -= 1
            eventOffset = i * timeBetweenEvents
            eventTime = startTime + timedelta(seconds=eventOffset)
            event = Event(deviceID=deviceID, state=curState, time=eventTime)
            db_session.add(event)
    
    db_session.commit()

deviceIDs = genDevices(10)
genEvents(deviceIDs, numberOfEvents=100)