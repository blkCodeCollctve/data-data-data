import bcc
import slack
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def list_commands():
    bot_commands = str(
        ([func for func in dir(slack.Slack) if callable(getattr(slack.Slack, func)) and not func.startswith("__")]))
    return render_template('index.html', bot_commands=bot_commands)


app.run()

def main():
    meetup = bcc.BCC()
    # meetup.joined_one_year_from_now()

    bot = slack.Slack()
    bot.test()


if __name__ == "__main__":
    main()
