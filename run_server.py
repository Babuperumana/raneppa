import os
import json
import flask
from telebot import types
from config import *
import bot_handlers

server = flask.Flask(__name__)

@server.route("/" + TOKEN, methods=["POST"])
def get_message():
    j = flask.request.stream.read().decode("utf-8")
    print(json.dumps(json.loads(j), indent=4))
    bot.process_new_updates([types.Update.de_json(j)])
    return "!", 200


@server.route("/", methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN))
    return "Hello from Heroku!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
