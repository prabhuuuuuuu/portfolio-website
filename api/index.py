from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

def handler(event, context):
    return app