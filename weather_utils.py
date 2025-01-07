import requests

# OpenCage API key
GEOCODING_API_KEY = ""

def get_coordinates(city):
    """
    Fetch latitude and longitude for a given city using OpenCage API.
    """
    url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={GEOCODING_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                latitude = data["results"][0]["geometry"]["lat"]
                longitude = data["results"][0]["geometry"]["lng"]
                return latitude, longitude
            else:
                return None, None
        else:
            return None, None
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def get_weather_by_city(city):
    """
    Fetch current weather for a given city using Open-Meteo API.
    """
    latitude, longitude = get_coordinates(city)
    if latitude is None or longitude is None:
        return f"Sorry, I couldn't find coordinates for {city}. Please try another city."

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data["current_weather"]
            temp = weather["temperature"]
            windspeed = weather["windspeed"]
            return f"The current weather in {city.capitalize()} is {temp}°C with a wind speed of {windspeed} km/h."
        else:
            return "Sorry, I couldn't fetch the weather information right now."
    except Exception as e:
        return f"An error occurred while fetching weather data: {str(e)}"
