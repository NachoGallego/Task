from fastapi.testclient import TestClient
from main import api  

client = TestClient(api)


def test_get_all_cars():
    response = client.get("/allCars")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]
    assert "bookingDates" in response.json()[0] # Each car have an id and bookingDates field


def test_get_available_cars_with_booked_date():
    response = client.get("/car", params={"date": "2025-06-20"})
    assert response.status_code == 200
    available_cars = response.json()
    assert isinstance(available_cars, list)
    assert 1 not in available_cars   # For the input date, Car 1 should not be available


def test_get_available_cars_with_free_date():
    response = client.get("/car", params={"date": "2025-06-25"})
    assert response.status_code == 200
    available_cars = response.json()
    assert isinstance(available_cars, list)
    assert 1 in available_cars and 2 in available_cars # For the input date, car 1 or 2 should be available


def test_get_available_cars_with_invalid_date():
    response = client.get("/car", params={"date": "invalid-date"})
    assert response.status_code == 422  #Should fail 


def test_car_booking_valid_date():
    response = client.post("/carBooking/2025-06-30")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data # For a date, booking should be successful


def test_car_booking_invalid_date_format():
    response = client.post("/carBooking/not-a-date")
    assert response.status_code == 200  
    assert response.json() == {"error": "Invalid date. Use format YYYY-MM-DD."} #Should fail 
