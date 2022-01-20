#!/bin/python

# library flask
from flask import Flask, request, jsonify

app = Flask(__name__)

# membuat rute dan methods
@app.route("/",methods=['GET'])
def home():
    return "halo world"
