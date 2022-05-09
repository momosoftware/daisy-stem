# Stem
## Web Logging Server for Daisy

# Imports
import os

from flask import Flask, render_template, request, flash, jsonify, request
import functools
from db import db_session
from models import Event, Device

# Constants
DAISY_FLOWER_SECRET = os.environ.get('DAISY_FLOWER_SECRET')
DAISY_ROOTS_SECRET = os.environ.get('DAISY_ROOTS_SECRET')

def apiKeyIsValid(request, client):
    if client == 'roots' and request.headers.get('X-DAISY_ROOTS_SECRET') and request.headers.get('X-DAISY_ROOTS_SECRET') == DAISY_ROOTS_SECRET:
        return True
    elif client == 'flower' and request.headers.get('X-DAISY_FLOWER_SECRET') and request.headers.get('X-DAISY_FLOWER_SECRET') == DAISY_FLOWER_SECRET:
        return True
    else:
        return False

def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if request.method == "POST" and apiKeyIsValid(request, 'roots'):
            return func(*args, **kwargs)
        elif request.method == "GET" and apiKeyIsValid(request, 'flower'):
            return func(*args, **kwargs)
        else:
            return {"message": "The provided API key is not valid"}, 403
    return decorator



app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['GET'])
def home():
    return '<h1>yes hello</h1><h2>api endpoints</h2><ul><li><a href="/api/v1/devices">Devices</a></li><li><a href="/api/v1/events">Events</a></li></ul>'

@app.route('/api/v1/events', methods=['GET'])
@api_required
def events():
    #reqBody = request.json
    
    # convert to list of dicts
    results = [r._asdict() for r in Event.query.all()]
    return jsonify(results)

@app.route('/api/v1/devices', methods=['GET'])
@api_required
def devices():
    #reqBody = request.json
    

    # convert to list of dicts
    results = [r._asdict() for r in Device.query.all()]
    return jsonify(results)

# scene selection
@app.route('/api/v1/logEvent', methods=['POST'])
@api_required
def lampPower(switch):
    if request.headers.get('DAISY_ROOTS_SECRET') == DAISY_ROOTS_SECRET:
        # add to db
        return 'ok', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    