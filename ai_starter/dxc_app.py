from flask import Flask
import flask
from . import app
from io import StringIO
import json
import sys
import os
from flask_jsonpify import jsonpify
import pandas as pd
from dxc import ai


#-------- ROUTES GO HERE -----------#
@app.route('/')
def welcome():
    return 'Welcome to DXC Industrialized AI Starter'

@app.route('/read', methods=["GET"])
def Search():
    # embed the query for calcluating the similarity
    typ = str(flask.request.args.get('type'))
    print(typ)
    loc = str(flask.request.args.get('loc'))
    print(loc)
    url = str(flask.request.args.get('url'))
    print(url)
    
    if (loc == "remote"):
        if (typ== "csv"):
            #print(1)
            df=ai.read_data_frame_from_remote_csv(url)
            #df = pd.read_csv(url)
            JSONP_data = df.to_json()
        elif (typ== "json"):
            print('json input')
            df=ai.read_data_frame_from_remote_json(url)
            #df = pd.read_json(url)
            JSONP_data = df.to_json()

    # elif (loc== "local"):
    #      if (typ== "csv"):
    #         df=ai.read_data_frame_from_local_csv()
    #         JSONP_data = df.to_json()
    #     elif (inp["type"]== "json"):
    #         df=ai.read_data_frame_from_local_json()
    #df_list = df.values.tolist()
    
    return JSONP_data

