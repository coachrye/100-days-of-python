import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = "8f988de38555d84cb2a2e7717fba38a3"
api_key = os.environ.get("OWM_API_KEY")
# Manila
# MY_LAT = 14.537752
# MY_LONG = 121.001381

# Rainy Place
MY_LAT = 45.955559
MY_LONG = 9.764700

account_sid = "AC7115bff990fa73314af08fc29b00b7ea" # os.environ['TWILIO_ACCOUNT_SID']
auth_token = "d91e21ebb42396eed12888ee7a393643" # os.environ['TWILIO_AUTH_TOKEN']
# Number :  +18566175895


# https://api.openweathermap.org/data/2.5/onecall?lat=14.537752&lon=121.001381&appid=8f988de38555d84cb2a2e7717fba38a3
# Twilio Fail Safe: J-TLK8ruAxV8YPR3MgHKdYDHiL9jT6Bw6kvVKBOt

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly = weather_data["hourly"]

will_rain = False

# for _ in range(0, 13):
#     print(hourly[_]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. Remember to bring an ☔️️",
        from_="+18566175895",
        to="+639062075201"
    )

    print(message.status)
else:
    print("All good!")
