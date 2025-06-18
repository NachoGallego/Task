from fastapi import FastAPI,Query
from datetime import datetime
import json


with open("cars.json", "r") as file:
    cars = json.load(file)

api = FastAPI()



@api.get("/allCars")
def get_cars():
    return cars

@api.get("/car")


def get_available_cars(date):
    input_date = datetime.strptime(date, "%Y-%m-%d").date()
    filtered_cars = []

    for car in cars:
        is_reserved = False

        for date_str in car["bookingDates"]:
            
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if date == input_date:
                    is_reserved = True
                    break  
             

        if not is_reserved:
            filtered_cars.append(car)

    return filtered_cars


@api.post("/carBooking/{bookingDate}")
def update_car_booking(bookingDate: str):
    try:
        input_date = datetime.strptime(bookingDate, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date. Use format YYYY-MM-DD."}

    for car in cars:
        if bookingDate not in car["bookingDates"]:
            car["bookingDates"].append(bookingDate)
            return {"message": f"Booking saved for car {car['id']}."}
        
    return {"message": "No cars available for that date."}
    
   