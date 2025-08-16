from ctypes.wintypes import DOUBLE

from sqlalchemy import Integer, Column, String, Double, TIMESTAMP
from tools.database import Base

class WeatherRecord(Base):
    __tablename__ = "weather_records"
    id = Column(Integer, primary_key=True, autoincrement=True)
    temp_min = Column(Double, nullable=False)
    pressure = Column(Integer,nullable=False)
    feels_like = Column(Double, nullable=False)
    wind = Column(Double, nullable=False)
    city = Column(String(255), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)


    def __repr__(self):
        return f"{self.temp_min} - {self.pressure} - {self.feels_like} - {self.wind} - {self.city} - {self.timestamp}"
