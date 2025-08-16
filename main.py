from services.mysql import add_record
from services.weather_api import fetch_weather
from services.excel import append_to_excel
import time

from tools.database import engine, Base

Base.metadata.create_all(engine)


while True:
    result = fetch_weather()
    # append_to_excel(result)
    add_record(result)
    time.sleep(5)