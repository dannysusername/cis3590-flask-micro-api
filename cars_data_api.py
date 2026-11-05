from flask import Flask, jsonify, request
import pandas as pd

# Load the CSV once when the server starts
df = pd.read_csv('cars.csv')

app = Flask(__name__)


# welcome message
@app.route('/hello')
def hello():
    return jsonify({'message': 'Welcome to my cars API'}), 200


# GET returns the first 10 cars, POST adds a new car
@app.route('/data', methods=['GET', 'POST'])
def data():
    global df

    if request.method == 'POST':
        new_car = request.get_json()
        if not new_car or 'CarName' not in new_car or 'price' not in new_car:
            return jsonify({'error': 'need CarName and price'}), 400

        new_car['car_ID'] = int(df['car_ID'].max()) + 1
        df = pd.concat([df, pd.DataFrame([new_car])], ignore_index=True)
        return jsonify({'message': 'car added', 'car': new_car}), 201

    cars = df[['car_ID', 'CarName', 'fueltype', 'price']].head(10)
    return jsonify(cars.to_dict(orient='records')), 200


@app.route('/cars')
def get_cars():
    return jsonify(df.head(10).to_dict(orient='records'))


@app.route('/manufacturers')
def manufacturers():
    return jsonify(df['CarName'].str.split().str[0].unique().tolist())


@app.route('/cars/prices')
def cars_prices():
    return jsonify(df[['CarName', 'price']].to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
