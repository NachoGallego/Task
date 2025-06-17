from fastapi import FastAPI,Query
from datetime import datetime

api = FastAPI()

cars = [
    {"id": 1, "bookingDates":["2025-06-01", "2025-06-05", "2025-06-10" ]},
    {"id": 2, "bookingDates":[ ]},
    {"id": 3, "bookingDates":["2025-06-02", "2025-06-06 "]},
    {"id": 4, "bookingDates":["2025-06-03", "2025-06-07", "2025-06-15" ]}]

@api.get("/")
def index():
    return {"message": "Hello, World!"}

@api.get("/allCars")
def get_cars():
    return cars

@api.get("/car")
def get_car_by_booking_date(bookingDate: str = Query(...)):
    try:
        input_date = datetime.strptime(bookingDate, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date. Use format YYYY-MM-DD."}

    filtered_cars = []
    for car in cars:
        
        for date_str in car["bookingDates"]:
            try:
                print(f"Input Date: {bookingDate}")
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if date == input_date:
                    filtered_cars.append(car)
                    break
            except ValueError:
                continue
    return filtered_cars

@api.post("/carBooking/{bookingDate}")
def update_car_booking(bookingDate: str, car_id: int):
    try:
        input_date = datetime.strptime(bookingDate, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date. Use format YYYY-MM-DD.."}

    for car in cars:
        if car["id"] == car_id:
            if bookingDate not in car["bookingDates"]:
                car["bookingDates"].append(bookingDate)
                return {"message": "Booking saved."}
            else:
                return {"message": "Date not available for this car."}
    
    return {"error": "Carn not found."}