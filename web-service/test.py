import predict
import requests

ride = {
    "PULocationID":1,
    "DOLocationID":2,
    "trip_distance": 10
}

# print("Duration: ", duration)
url = "http://localhost:9696/predict"
response = requests.post(url, json=ride)
print(response.json())