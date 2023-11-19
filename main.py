from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('192.168.0.102', 30000)
db = client['lab16']
collection = db['weather']

@app.route('/weather', methods=['GET'])
def get_weather_by_city():
    city = request.args.get('city')
    day = request.args.get('day')

    if city is None:
        return jsonify({"error": "City parameter missing"}), 400

    query = {"city": city}

    weather_data = list(collection.find(query))

    if not weather_data:
        return jsonify({"error": "No data found for this city and day"}), 404

    # Extract only necessary fields from the documents
    formatted_data = [
        {
            "_id": str(data["_id"]),
            "city": data["city"],
            "date": data["date"],
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "max_temp": data["max_temp"],
            "min_temp": data["min_temp"]
        }
        for data in weather_data
    ]

    return jsonify(formatted_data)

if __name__ == '__main__':
    app.run(debug=True)
