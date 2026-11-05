import requests

base_url = 'http://localhost:8080'

# test GET /hello
response = requests.get(f'{base_url}/hello')
print(response.status_code, response.json())

# test GET /data
response = requests.get(f'{base_url}/data')
print(response.status_code, response.json())

# test POST /data
new_car = {'CarName': 'tesla model3', 'fueltype': 'electric', 'price': 38990}
response = requests.post(f'{base_url}/data', json=new_car)
print(response.status_code, response.json())
