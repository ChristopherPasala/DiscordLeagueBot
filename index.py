# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:26:58 2020

@author: chris
"""

import urllib3
import json
import certifi

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
api_key = 'RGAPI-8a27fbd9-12df-4cad-9402-86b7729598db'

region = 'na1'
name = (str)(input("What is the summoner name: "))

while (name.find(' ')!=-1):
    name = name[:name.find(' ')]+"%20"+name[name.find(' ' )+1:]
print(name)

URL1 = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+"?api_key="+api_key

r1 = http.request('GET', URL1)

rJson = json.loads(r1.data.decode("utf-8"))
print(rJson)
SumID = rJson['accountId']

print(SumID)
champion =(str)(input("What is the Champion ID: "))

URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+SumID+"?champion="+champion+"&api_key="+api_key
r = http.request('GET', URL)

rJson = json.loads(r.data.decode("utf-8"))
print(rJson['totalGames'])