
from flask import Flask, request, send_from_directory, Blueprint
import Calculations as calc
import requests
import json

# ngrok http 80

# api = Blueprint('account_api', __name__)
app = Flask(__name__)


@app.route('/api/cost', methods=['POST'])
def get_cost():
    try:
        x = request.json['Long']
        y = request.json['Lat']
        acres = request.json['Acres']

        print(x, y, acres)

        # Do whatever here with variables
        results = calc.prediction('current.joblib', [x, y, acres])

        # status_code = requests.post('their_endpoint', json={'output': '12000'})
        # if status_code.status_code == 200:
            # print('We yeet data to front end bois')
        #return 'Received'
        return json.dumps({'get_cost': True, "cost": str(float(results))}), 200, {'ContentType': 'application/json'}

    except Exception as e:
        return json.dumps({'get_cost': False}), 400, {'ContentType': 'application/json'}


app.run(host='0.0.0.0', port='80')
