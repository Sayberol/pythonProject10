from os import abort

from flask import Flask, render_template, request

from coursework2_source.funcs import load_data

posts, comments, bookmarks = load_data()

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', posts=posts)


@app.route("/search/s=")
def page_search():
    return render_template('search.html', posts=posts, comments=comments, bookmarks=bookmarks)


@app.route("/users/<username>")
def page_users():
    return render_template('user-feed.html', posts=posts, comments=comments, bookmarks=bookmarks)


app.run()
