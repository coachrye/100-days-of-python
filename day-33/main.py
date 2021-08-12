import requests
from datetime import datetime


MY_LAT = 14.537752
MY_LONG = 121.001381
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# # data = response.json()["iss_position"]
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# print(data)
#
# print(longitude)
# print(latitude)
#
# iss_position = (longitude, latitude)
# print(iss_position)


# https://www.udemy.com/course/100-days-of-code/learn/lecture/21214136#notes

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# sunrise = data["results"]["sunrise"]
# print(sunrise.split("T")[1].split(":")[0])
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now = datetime.now()

print(time_now.hour)