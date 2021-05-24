import random

from essential_generators import DocumentGenerator

gen = DocumentGenerator()

#Documentation provided at https://api.slack.com/methods/chat.postMessage

class Resp:

    PAYLOAD = {
        "type": "section",
        "text": {
            "type": "plain_text",
            "text": ("So this came to my thought...\n\n"
            ),
        },
    }

    def __init__(self, channel):
        self.channel = channel

    def genText(self):

        text = gen.paragraph()

        return {"type": "section", "text": {"type": "plain_text", "text": text}},

    def generate_payload(self):

        return {
            "channel": self.channel,
            "blocks": [
                self.PAYLOAD,
                *self.genText(),
            ],
        }

