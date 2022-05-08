# Stem
## Web Logging Server for Daisy

# Imports
import os

from flask import Flask, render_template, request, flash, jsonify
from db import db_session
from models import Event, Device

# Constants
DAISY_FLOWER_SECRET = os.environ.get('DAISY_FLOWER_SECRET')
DAISY_ROOTS_SECRET = os.environ.get('DAISY_ROOTS_SECRET')

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['GET'])
def home():
    return jsonify({'yes':'hello'})

@app.route('/events', methods=['GET'])
def events():
    #reqBody = request.json
    
    # convert to list of dicts
    results = [r._asdict() for r in Event.query.all()]
    return jsonify(results)

@app.route('/devices', methods=['GET'])
def devices():
    #reqBody = request.json
    

    # convert to list of dicts
    results = [r._asdict() for r in Device.query.all()]
    return jsonify(results)

# scene selection
@app.route('/logEvent', methods=['POST'])
def lampPower(switch):
    if request.headers.get('DAISY_ROOTS_SECRET') == DAISY_ROOTS_SECRET:
        # add to db
        return 'ok', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    