from fastapi import FastAPI,HTTPException
from datetime import datetime
import json
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




with open("cars.json", "r") as file: #Load data from JSON file
    cars = json.load(file)
    logger.info("Loaded %d cars from cars.json", len(cars))

api = FastAPI()



@api.get("/allCars") #Returns a list of all cars and their booking dates
def get_cars():
    logger.info("GET /allCars called")
    return cars

@api.get("/car") #Returns a list of available cars for a given date
def get_available_cars(date):
    logger.info("GET /car called with date=%s", date)
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date. Use format YYYY-MM-DD."
        )
    filtered_cars = []

    for car in cars:
        is_reserved = False

        for date_str in car["bookingDates"]:
            
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if date == input_date:
                    is_reserved = True
                    break  
             

        if not is_reserved:
            filtered_cars.append(car["id"])

    return filtered_cars


@api.post("/carBooking/{bookingDate}") #Books the first available car for a given date
def update_car_booking(bookingDate: str):
    logger.info("POST /carBooking/%s called", bookingDate)
    try:
        input_date = datetime.strptime(bookingDate, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date. Use format YYYY-MM-DD."
        )

    for car in cars:
        if bookingDate not in car["bookingDates"]:
            car["bookingDates"].append(bookingDate)
            return {"message": f"Booking saved for car {car['id']}."}
        
    return {"message": "No cars available for that date."}
    
   