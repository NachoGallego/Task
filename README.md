# BL task

API containing 3 endpoints for retrievig information about a car rental business. It consists on:

2 GET request to retrieve first, all the cars in the JSON file and second, all the cars available for a given date. 

1 POST request to add a booking date to the first car available.



## Install

from source
```bash
git clone https://github.com/NachoGallego/Task.git BLtask
cd BLtask
make install
```



## Executing



```bash
$ uvicorn BLtask:app
```



## API

Access http://127.0.0.1:9999/docs after running the API to check all the documentation available about the endpoints.

- allCars: Retrieves a list of cars and their booked dates. 
Ex: http://127.0.0.1:9999/allCars

- car: Get all available cars for a given date.
Ex: http://127.0.0.1:9999/car?date=2025-06-07

- carBooking: Books a car for a given date.
Ex: http://127.0.0.1:9999/carBooking/2025-06-07




## Testing

For testing I have used the library pytest.

Testing:

- test_get_all_cars: Retrieves all cars.
- test_get_available_cars_with_booked_date: For a given date retrieves all available cars but car with id = 1.
- test_get_available_cars_with_free_date: For a given date retrieves all available cars but car with id = 1 and id = 2 should be in the list.
- test_get_available_cars_with_invalid_date: Forced error with invalid format date.
- test_car_booking_valid_date: Succesfull booking.
- test_car_booking_invalid_date_format: Forced error with invalid format date.

``` bash
=================================================== short test summary info =================================================== 
FAILED test_main.py::test_get_available_cars_with_invalid_date - assert 400 == 422
FAILED test_main.py::test_car_booking_invalid_date_format - assert 400 == 200
================================================= 2 failed, 4 passed in 0.80s ================================================

```

