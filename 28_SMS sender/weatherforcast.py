import requests
from twilio.rest import Client

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Your api key"
account_sid = "your twilio account sid"
auth_token = "Your twilio auth token"

parameters = {
    "lat": 23.610182,
    "lon": 85.279938,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(api_endpoint, parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

will_rain = False
weather = [i["weather"][0]["id"] for i in weather_data["list"]]
for i in weather:
    if i < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain take an umbrella",
        from_="+15109014405",
        to="Phone that you have verified by twilio or used to log in into the twilio website"
    )
    print(message.status)
