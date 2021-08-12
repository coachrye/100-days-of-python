import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "basda923ercxzm13"
USERNAME = "coachrye"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "exercise1"

graph_params = {
    "id": GRAPH_ID,
    "name": "Push Ups",
    "unit": "push",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Manila",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

now = datetime.now()
today = now.strftime('%Y%m%d')

pixel_params = {
    "date": today,
    "quantity": input("How many pushups did you do today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

pixel_update_params = {
    "quantity": "5",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
