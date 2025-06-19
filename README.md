# BL task

API containing 3 endpoints for retrievig information about a car rental business.


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

Access http://127.0.0.1:9999/docs after running the API to check ll the documentation available about the endpoints.

- allCars: Retrieves a list of cars and their booked dates. 
Ex: http://127.0.0.1:9999/allCars

- car: Get all available cars for a given date.
Ex: http://127.0.0.1:9999/car?date=2025-06-07

- carBooking: Books a car for a given date.
Ex: http://127.0.0.1:9999/carBooking/2025-06-07




## Testing

For testing I have used the librry pytest. 

=================================================== short test summary info =================================================== 
FAILED test_main.py::test_get_available_cars_with_free_date - AssertionError: assert ('1' in [1, 2, 3, 4, 5, 6, ...] or 'car2' in [1, 2, 3, 4, 5, 6, ...])
FAILED test_main.py::test_get_available_cars_with_invalid_date - assert 400 == 422
FAILED test_main.py::test_car_booking_invalid_date_format - assert 400 == 200
================================================= 3 failed, 3 passed in 0.81s =================================================



