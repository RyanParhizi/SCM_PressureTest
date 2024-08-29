import requests

# The URL of your Flask server
url = 'http://192.168.1.118:5001'

# Your JSON data
data = {
    "time": 100,
    "pressure": 30
}

# Sending POST request with JSON data
response = requests.post(url, json=data)

# Print the response from the server
print(response.json())