from flask import Flask, request, jsonify
import requests
import os
import openai
from flask_cors import CORS
from dotenv import dotenv_values
# from langchain.llms import OpenAI
# from agent import llm as langchain_llm, agent

app = Flask(__name__)
# CORS(app, origins='http://learn-gpt.s3-website-us-east-1.amazonaws.com/')
CORS(app, origins='http://localhost:3000')

config = dotenv_values(".env")
api_key = config["openai_key"]

openai.api_key = api_key

@app.route('/')
def hello():
    return 'hello world'

@app.route('/chat', methods=['POST'])
def chat():
    # Get the query from the request body
    query = request.json.get('query', '')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query}
        ]
    )   

    completion_text = completion.choices[0].message.content

    # Return the response from the Flask endpoint
    return jsonify({'response': completion_text})

# @app.route('/testing', methods=['POST'])
# def testing():
#     query = request.json.get('query', '')

#     # response = langchain_llm(query)

#     response = agent.run(query)

#     return jsonify({'response': response})


if __name__ == '__main__':
    app.run()