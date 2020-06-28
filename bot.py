from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pprint import pprint

app = Flask(__name__)


@app.route('/reply', methods=['POST'])
def reply():
        pprint(request.values)
        resp = MessagingResponse()
        resp.message("What's up, Twilio?")
        return str(resp)
