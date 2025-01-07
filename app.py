from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from weather_utils import get_weather_by_city

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/weather", methods=["POST"])
def weather():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "Please enter a valid city name."}), 400

    # Fetch weather for the city
    response = get_weather_by_city(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
