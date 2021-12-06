import flask
from . import app
from . import readdata
import json
import pandas as pd
#from dxc import ai


#-------- ROUTES GO HERE -----------#
@app.route('/')
def welcome():
    return 'Welcome to DXC Industrialized AI Starter'

JSONP_data = ' '

@app.route('/read', methods=["GET"])
def Search():
    # embed the query for calcluating the similarity
    typ = str(flask.request.args.get('type'))
    loc = str(flask.request.args.get('loc'))
    url = str(flask.request.args.get('url'))
    
    if (loc == "remote"):
        if (typ== "csv"):
            df=readdata.read_data_frame_from_remote_csv(url)
            JSONP_data = df.to_json()
        elif (typ== "json"):
            df= readdata.read_data_frame_from_remote_json(url)
            JSONP_data = df.to_json()
    if (loc == "local"):
        if (typ== "csv"):
            df = readdata.read_data_frame_from_local_csv(url)
            JSONP_data = df.to_json()
    
    return JSONP_data 

