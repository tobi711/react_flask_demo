import time 
from flask import Flask, render_template, request
import json 
import werkzeug
import requests
from requests.structures import CaseInsensitiveDict
#own files and classes
from visitor_data import Visitorflow


api =  Flask(__name__)

@api.route('/time')
def get_current_time():
    return {'time':time.time()}


@api.route('/jsondata', methods = ['GET'])
def json_return():
    return {
        "userID":1,
        "title": ['1','2','3','4'],
        "completed":False
        }


