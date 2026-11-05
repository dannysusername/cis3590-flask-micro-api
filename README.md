# CIS 3590 Flask Micro-API

Flask API that uses the cars.csv dataset.

Routes:
- /hello - welcome message
- /data - GET gets the first 10 cars, POST adds a car (needs CarName and price)
- /cars, /manufacturers, /cars/prices - from class

To run:
pip install -r requirements.txt
python cars_data_api.py
then in another terminal run python client_app3.py to test it

Screenshots are in the screenshots folder.
