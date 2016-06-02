# #Hack logging for debug logs
# from __future__ import print_function
# import sys

from flask import Flask, json
from flask import request

import models
import os
import requests
import player_stat_loader
import threading

app = Flask(__name__)
# app.json_encoder = models.JsonEncoder TODO: may be needed for custom python object deserialization

@app.route("/api/detail.json", methods=["GET", "POST"])
def data():
    playerName = request.form['text']
    responseUrl = request.form['response_url']

    thr = threading.Thread(target=coroutineForPlayerStatsResponse, args=(playerName, responseUrl), kwargs={})
    thr.start() # will run the load and

    return "" #return immediately with empty body

def coroutineForPlayerStatsResponse(playerName, responseUrl):
    r = requests.post(responseUrl, json = { "text": "OHAI " + playerName + ": " + str(player_stat_loader.getPlayerData(playerName)), "response_type": "in_channel", })

    print r.url
    print r.text


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
