from unicodedata import name
from flask import Flask, jsonify, request

app = Flask(__name__)

destination = [
    {'city': "Solapur", "state": "Maharashtra", "pincode": "413006", "name": "Dmart", "categories": "Shopping", "rating": "4"}]


@app.route('/destination', methods=['GET'])
def getDestinations():
    return jsonify(destination)


@app.route('/destination', methods=['POST'])
def addDestination():
    destination.append(request.get_json())
    return '', 201


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
