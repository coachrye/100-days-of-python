import requests
import json
from datetime import datetime
import os

# # https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
# from decouple import config
# APP_ID = config('APP_ID')
# API_KEY = config('API_KEY')

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query": input("Tell me which exercises you did: "),
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
res = json.loads(response.text)

sheety_endpoint = "https://api.sheety.co/9667f7149fe756ff212f8ac1bee7e0b7/myWorkouts/workouts"

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

BEARER_TOKEN = "thisissomekindofamazingsecrettoken"
sheety_headers = {"Authorization": "Bearer thisissomekindofamazingsecrettoken"}

for log in res['exercises']:
    sheety_params = {
      "workout": {
          "date": today,
          "time": time,
          "exercise": log['name'].title(),
          "duration": log['duration_min'],
          "calories": log['nf_calories'],
      }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
    # print(response.text)
