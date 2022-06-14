import flask
from flask import Flask, render_template

app = Flask(__name__)

BLOG_NAME = "EntropistA"


@app.route("/")
def index():
    return render_template("index.html", blog_name=BLOG_NAME)


@app.route("/about.html")
def about():
    return render_template("about.html", blog_name=BLOG_NAME)


@app.route("/contact.html")
def contact():
    return render_template("contact.html", blog_name=BLOG_NAME)


@app.route("/post.html")
def post():
    return render_template("post.html", blog_name=BLOG_NAME)
