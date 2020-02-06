from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    a = 1 + 1
    return f"Hello world = {a}"


if __name__ == "__main__":
    app.run()