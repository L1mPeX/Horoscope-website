# coding UTF-8
from bottle import route, run, view
from datetime import datetime as dt
from random import randint
from horoscope import generate_prophecies


@route("/")
@view("predictions")
def index():
    now = dt.now()
    x = randint(0, 4)
    l = generate_prophecies()
    return {
        "date": f"{now.year}-{now.month}-{now.day}",
        "predictions": l[x],
        "x": x
    }

run(
    host="localhost",
    port=8080,
    autoreload=True
)
