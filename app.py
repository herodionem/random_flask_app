from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    a = 1 + 1
    return f"Hello world = {a}"

@app.route("/get-html-from-google")
def get_html_from_google():
    content = requests.get("https://www.google.com").content
    return content


if __name__ == "__main__":
    app.run()