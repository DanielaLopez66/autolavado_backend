'''
Docstring for models.modelVehiculo
'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from config.db import Base

class Vehiculo(Base):
    '''Modelo del vehiculo'''
    __table__ = "tbb_vehiculo"

    id = Column
