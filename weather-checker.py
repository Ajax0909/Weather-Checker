import requests
import sys

API_KEY = "YOUR_KEY" #Get your API key from OpenWeather and replace it here.
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" 
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print(f"\n🌤  Weather in {city_name}, {country}")
        print(f"🌡  Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"☁️  Condition: {weather.capitalize()}")
        print(f"💧  Humidity: {humidity}%")
        print(f"🌬  Wind Speed: {wind} m/s\n")
    else:
        print("❌ Error fetching weather data. Check city name or API key.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city_name>")
    else:
        city = " ".join(sys.argv[1:])
        get_weather(city)

user_city = input("Enter city name: ")
get_weather(user_city)
