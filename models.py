from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    events = relationship("Event", back_populates="device")

    def __init__(self, name=None, location=None):
        self.name = name
        self.location = location

    def __repr__(self):
        return f'<Device name={self.name!r}, location={self.location!r}>'

    def _asdict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    deviceID = Column(Integer, ForeignKey('devices.id'))
    state = Column(Integer)
    device = relationship("Device", back_populates="events")

    def __init__(self, deviceID=None, state=None, time=None):
        self.deviceID = deviceID
        self.state = state
        if time:
            self.time = time
        else:
            self.time = datetime.now()

    def __repr__(self):
        return f'<Event deviceID={self.deviceID!r}, state={self.state!r}>'

    def _asdict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
