from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot=ChatBot('trainmaster')
trainer=ListTrainer(bot)
for knowledeg in os.listdir('base'):

	BotMemory = open('base/'+ knowledeg, 'r').readlines()
	trainer.train(BotMemory)

app = Flask(__name__)
arr=[]
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    f = open("backup.txt", "a+")

    arr.append(userText)
    for i in arr:
        f.write(i + "\n")

    f.close()
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run()
