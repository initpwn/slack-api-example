import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from bot import Resp

app = Flask(__name__)

slack_events_adapter = SlackEventAdapter("474ecafa4c7785cff692e822ad364331", "/slack/events", app)

BoS = ['say something bot','hey bot, say something','hey bot say something']

slack_web_client = WebClient(token='xoxb-229090703222-2109477858689-s5rfjwJyckfzybBJVaY5Eju4')

def generate_response(channel):
    resp_gen = Resp(channel)

    text = resp_gen.generate_payload()

    slack_web_client.chat_postMessage(**text)

@slack_events_adapter.on("message")
def message(payload):

    event = payload.get("event", {})

    text = event.get("text")

    if text.lower() in BoS:
        channel_id = event.get("channel")
        return generate_response(channel_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
