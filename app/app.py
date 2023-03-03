# python imports 
import os
from typing import List, Dict
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# slack imports 
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# open ai imports 
import openai
print(SLACK_APP_TOKEN)
app = App(token=SLACK_BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

message_queue = []

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(event,say):
    print("App was mentioned")
    say("Hi there!")

@app.event("message")
def handle_message(event, say):
    message_queue.append({"role": "user","content":event["text"]})
    print("Received message: "+ event["text"])
    response = gpt_response(message_queue)
    role, content = list(response.keys())[0],list(response.values())[0]
    message_queue.append({"role": role,"content":content})
    print("Message sent: "+ event["text"])
    say(list(response.values())[0])

def gpt_response(direct_message_history: List[Dict[str, str]], reset = 0) -> Dict[str, str]:
    if reset:
        global message_queue
        message_queue = []
    print("message",direct_message_history)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = direct_message_history
    )
    return {response['choices'][0]['message']['role']: response['choices'][0]['message']['content']}


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()