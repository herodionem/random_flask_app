from flask import Flask, request
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
    a = 1 + 1
    return f"Hello world = {a}"

@app.route("/random-cheese")
def random_cheese():
    cheeses = [
        'gouda',
        'swiss',
        'provolone',
        'brie',
        'bleu cheese',
        'sharp \'merican cheddar',
        'gorganzola',
    ]
    return cheeses[randint(0, len(cheeses) - 1)]


if __name__ == "__main__":
    app.run()