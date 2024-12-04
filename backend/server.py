import api_filter
from flask import Flask, request, jsonify, abort, Response
import boto3
from prometheus_client import generate_latest, REGISTRY, Counter


app = Flask("Omer API Server", static_url_path='')
app.secret_key = "12345678"
dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('omerappdb')
city_view_counter = Counter('city_views', 'Number of times each city has been viewed', ['city_name'])

@app.route('/metrics')
def metrics():
# Use the default registry, which contains only the default metrics
    return Response(generate_latest(REGISTRY), mimetype="text/plain")

@app.route('/', methods=["GET"])
def default():
    """Default route for / returning 200"""
    return {"status": 200}

@app.route('/api/', methods=["POST"])
def get_city():
    """Handle the api request, gets from the client the city and pass it to api_filter.py
    In addition filter the data to the related one and return it."""
    city = request.form.get('city')
    api_response = api_filter.api_request(city)
    if api_response == 404:
        abort(404)
    
    city_view_counter.labels(city_name=city).inc()

    response = api_response[0]  # Get the response
    days = response['days']  # Get the days array from the json
    filtered_data = {
        'resolvedAddress': response['resolvedAddress'],
        'address': response['address'],
        'days_day': [day['tempmax'] for day in days],
        'days_night': [day['tempmin'] for day in days],
        'humidity': [day['humidity'] for day in days],
        'country': api_response[1]  # Get the country
    }
    response = jsonify([filtered_data])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/store-weather/', methods=["POST"])
def store_weather():
    """Store weather data in DynamoDB"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    city = data.get("city")
    country = data.get("country")
    daily_weather = data.get("dailyWeather", [])

    if daily_weather:
        first_day_weather = daily_weather[0]
        
        # Extract the maximum temperature for the day using 'tempmax' field
        max_temp = daily_weather[0]['days_day'][0]        
        
        item = {
            "city": city,
            "country": country,
            "timestamp": data.get("timestamp"),
            "temp": max_temp  # Store the maximum temperature for the day
        }

        try:
            response = table.put_item(Item=item)
            return jsonify({"message": "Weather data stored successfully!"}), 200
        except Exception as e:
            app.logger.error(f"Error storing weather data: {str(e)}")
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "No daily weather data available"}), 400




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
