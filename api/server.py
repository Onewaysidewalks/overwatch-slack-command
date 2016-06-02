# #Hack logging for debug logs
# from __future__ import print_function
# import sys

from flask import Flask, json
from flask import request

import models
import os

app = Flask(__name__)
# app.json_encoder = models.JsonEncoder TODO: may be needed for custom python object deserialization

@app.route("/api/detail.json", methods=["GET", "POST"])
def data():
    return json.jsonify({ "text": "OHAI " + request.form['text'], "response_type": "in_channel", })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
