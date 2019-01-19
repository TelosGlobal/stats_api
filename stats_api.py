#!/usr/bin/python2.9

from flask import Flask, jsonify, abort, request, Response
import json
import requests
from functools import wraps
import subprocess

#VARS

#CryptoCompare unique API Key
apiKey = "YOUR_UNIQUE_KEY_HERE"

#The BP acct name you want to look for
myBP = "telosglobal1"

#Host IP
myHost = "10.120.86.18"

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def prods():

    p = subprocess.Popen("/ext/telos-build/telos/build/bin/teclos system listproducers -j -l 50 | jq '.rows[] | .owner, .total_votes, .producer_key'", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()

    return output

@app.route('/bprank', methods = ['GET'])
def bprank():

    url = "http://127.0.0.1:8888/v1/chain/get_producers"

    payload = "{\"json\":\"true\",\"limit\":\"50\"}"
    response = requests.request("POST", url, data=payload)

    bpOut = json.loads(response.text)

    output = "RANK  BP  VOTES  DIFF"

    #Set last votes to same as first ranked BP so diff will always be 0 for first record
        lVotes = int(round(float(bpOut["rows"][0]["total_votes"])/10000))

    for x in range(30):
        rRank = x + 1
        rOwner = str(bpOut["rows"][x]["owner"])
        rVotes = int(round(float(bpOut["rows"][x]["total_votes"])/10000))
        rDiff = lVotes - rVotes
        if x < 9:
            rOutput = " " + str(rRank) + ": " + rOwner + " " + str(format(rVotes, ',')) + " (" + str(format(rDiff, ',')) + ")"
        else:
            rOutput = str(rRank) + ": " + rOwner + " " + str(format(rVotes, ',')) + " (" + str(format(rDiff, ',')) + ")"
        if rOwner == myBP:
            rOutput = rOutput + " ****"
        output = output + "<br>" + rOutput
        lVotes = rVotes
        if x ==20:
            output = output + "<br>-------------------------"

    return output

#Get Rotation Info
@app.route('/rotation', methods = ['GET'])
def rotation():

    url = "http://127.0.0.1:8888/v1/chain/get_table_rows"

    payload = "{\"json\":\"true\",\"scope\":\"eosio\",\"code\":\"eosio\",\"table\":\"rotations\"}"
    response = requests.request("POST", url, data=payload)
    
    
    #print(response.text)
    parsed = json.loads(response.text)
    output = "Rotated Out: " + str(parsed['rows'][0]['bp_currently_out']) + "<br>Rotated In:  " + str(parsed['rows'][0]['sbp_currently_in']) + "<br>Next Rotate: "  + str(parsed['rows'][0]['next_rotation_time']) + " UTC<br>"
    #output = parsed['rows'][0]['bp_currently_out']

    return output

@app.route('/price', methods = ['GET'])
def price():

    #Get TLOS/EOS pair price
    resp = requests.get('https://api.chainrift.com/v1/Public/Market?symbol=TLOS/EOS')
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    #print(resp.json())
    returnString = json.loads(resp.text)
    tprice = returnString['data'][0]['last']

    #Get EOS Price 
    resp = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EOS&tsyms=USD&api_key=',apiKey)
    if resp.status_code != 200:
        # This means something went wrong.
               raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    #print(resp.json())
    returnString = json.loads(resp.text)
    eprice = returnString['USD']
    tlosPrice = eprice * tprice

    prices = "TLOS/EOS: ${0:.2f}".format(tprice)+" | EOS/USD: ${0:.2f}".format(eprice)+" | TLOS/USD: ${0:.2f}".format(tlosPrice)

    return prices

@app.route('/all', methods = ['GET'])
def bpall():

    url = "http://127.0.0.1:8888/v1/chain/get_producers"

    payload = "{\"json\":\"true\",\"limit\":\"50\"}"
    response = requests.request("POST", url, data=payload)

    bpOut = json.loads(response.text)

    output = "RANK  BP  VOTES  DIFF"

    #Set last votes to same as first ranked BP so diff will always be 0 for first record
    lVotes = int(round(float(bpOut["rows"][0]["total_votes"])/10000))

    for x in range(30):
        rRank = x + 1
               rOwner = str(bpOut["rows"][x]["owner"])
        rVotes = int(round(float(bpOut["rows"][x]["total_votes"])/10000))
        rDiff = lVotes - rVotes
        if x < 9:
            rOutput = " " + str(rRank) + ": " + rOwner + " " + str(format(rVotes, ',')) + " (" + str(format(rDiff, ',')) + ")"
        else:
            rOutput = str(rRank) + ": " + rOwner + " " + str(format(rVotes, ',')) + " (" + str(format(rDiff, ',')) + ")"
        if rOwner == myBP:
            rOutput = rOutput + " ****"
        output = output + "<br>" + rOutput
        lVotes = rVotes
        if x ==20:
            output = output + "<br>-------------------------"

    #Get Rotation
    url = "http://127.0.0.1:8888/v1/chain/get_table_rows"

    payload = "{\"json\":\"true\",\"scope\":\"eosio\",\"code\":\"eosio\",\"table\":\"rotations\"}"
    response = requests.request("POST", url, data=payload)

    #print(response.text)
    parsed = json.loads(response.text)
    output = output + "<br><br>-----------------------<br>Rotated Out: " + str(parsed['rows'][0]['bp_currently_out']) + "<br>Rotated In:  " + str(parsed['rows'][0]['sbp_currently_in']) + "<br>Next Rotate: "  + str(parsed['rows'][0]['next_rotation_time']) + " UTC<br>"
    #output = parsed['rows'][0]['bp_currently_out']

    #Get TLOS/EOS pair price
    resp = requests.get('https://api.chainrift.com/v1/Public/Market?symbol=TLOS/EOS')
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    #print(resp.json())
    returnString = json.loads(resp.text)
    tprice = returnString['data'][0]['last']

    #Get EOS Price 
    resp = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EOS&tsyms=USD&api_key=',apiKey)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    #print(resp.json())
    returnString = json.loads(resp.text)
    eprice = returnString['USD']
    tlosPrice = eprice * tprice

    prices = "TLOS/EOS: ${0:.2f}".format(tprice)+" | EOS/USD: ${0:.2f}".format(eprice)+" | TLOS/USD: ${0:.2f}".format(tlosPrice)

    output = output + "<br>------------------------<br>" + prices


    return output
    
    if __name__ == '__main__':
    app.run(host=myHost)
    
