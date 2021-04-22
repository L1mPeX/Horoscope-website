# coding UTF-8

from horoscope import generate_prophecies
from datetime import datetime as dt


def generate_page(head, body):
    page = f"<html> \n{head} \n {body} \n</html>"
    return page


def generate_head(title):
    head = f"<head> \n<meta charset='UTF-8'> \n<title> {title} </title>\n<head>"
    return head


def generate_body(header, paragraph):
    body = f"<body> \n<h1> {header} </h1> \n<p> {paragraph} </p>\n</body>"
    return body


def save_page(title, header, paragraph, output="index.html"):
    fp = open(output, "w")
    today = dt.now().date()
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraph=paragraph)
    )
    print(page, file=fp)
    fp.close()


today = dt.now().date()
save_page(
    title="Гороскоп на сегодня",
    header=f"Что день {today} готовит",
    paragraph=generate_prophecies(),
)
