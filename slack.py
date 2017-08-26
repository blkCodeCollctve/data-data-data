""" BCC Slack Api """
import os
from pprint import pprint
from slackclient import SlackClient


class Slack(object):
    def __init__(self):
        self.slack_token = os.environ["SLACK_API_TOKEN"]
        self.client = SlackClient(self.slack_token)

    def test(self):
        pprint(self.client.api_call(
            "chat.postMessage",
            channel="botfrey",
            text="Hi `yerp` :100: yas",
            reply_broadcast=True
        ))

