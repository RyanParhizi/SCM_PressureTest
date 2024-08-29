import requests
import json

# Define the server URL and port
url = 'http://192.168.1.118:5001/data'

# Create the JSON object to send
data = {
    "time": "2024-08-29T12:34:56Z",
    "pressure": 101.3
}

# Convert the data to a JSON string
json_data = json.dumps(data)

# Send the JSON object to the Flask server
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# Print the response from the server
print(response.json())