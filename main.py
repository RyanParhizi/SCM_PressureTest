from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

csv_file = 'data.csv'

@app.route('/')
def home():
    return('test')

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    time = data.get("time")
    pressure = data.get("pressure")

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time, pressure])

    return jsonify(200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)