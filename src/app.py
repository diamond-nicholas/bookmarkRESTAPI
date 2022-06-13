from flask import Flask, jsonify

# set environment
# export FLASK_ENV = developement

# set path
# export FLASK_ENV = app


# create an instance of flask
app = Flask(__name__)

@app.get('/')
def index():
    return jsonify({'message': 'hello world'})