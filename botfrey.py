import bcc
import slack
import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def list_commands():
    bot_commands = str(
        ([func for func in dir(slack.Slack) if callable(getattr(slack.Slack, func)) and not func.startswith("__")]))
    return render_template('index.html', bot_commands=bot_commands)


@app.route('/test/')
def test_msg():
    bot = slack.Slack()
    bot.test()

    return redirect(url_for('list_commands'))


def main():
    meetup = bcc.BCC()
    # meetup.joined_one_year_from_now()

    bot = slack.Slack()
    bot.test()


if __name__ == "__main__":
    # For testing purposes
    # main()

    app.run(debug=True)
