# import time

# import redis
# from flask import Flask, jsonify, render_template, request

# app = Flask(__name__)
# cache = redis.Redis(host='redis', port=6379)

# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)

# def home():
#   return "Hello, This is Flask Application"
# if __name__ == "__main__":
#   app.run()
    
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key  = "sk-proj-svUGaBjxtyLkhJK9rO7gT3BlbkFJaPFZevE3Nseie5zEni1c"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = get_completion(userText)
    #return str(bot.get_response(userText))
    return response

if __name__ == "__main__":
    app.run()
