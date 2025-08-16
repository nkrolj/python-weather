from models.WeatherRecord import WeatherRecord
from tools.database import Session

def add_record(result):
    with Session() as session:
        new_record = WeatherRecord(
            temp_min=result["temp_min"],
            pressure=result["pressure"],
            feels_like=result["feels_like"],
            wind=result["wind"],
            city=result["city"],
            timestamp=result["timestamp"]
        )
        session.add(new_record)
        session.commit()
        print("Zapisano w bazie")