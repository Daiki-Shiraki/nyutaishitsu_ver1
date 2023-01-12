# -*- coding: utf-8 -*-
import requests
import json
import config

def getData():
    url = config.url
    return json.loads(response.text)

DB = getData()
#for db in DB:
 #   if db["pass2"] != "":
  #      print(db)