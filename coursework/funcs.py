import json
from pprint import pprint


def load_data():

    with open('data/data.json', 'r', encoding='utf-8') as fp:
        posts = json.load(fp)

    with open('data/comments.json', 'r', encoding='utf-8') as fp:
        comments = json.load(fp)

    posts = comments_in_posts(posts, comments)

    with open('data/bookmarks.json', 'r', encoding='utf-8') as fp:
        bookmarks = json.load(fp)

    return posts, comments, bookmarks


def comments_in_posts(posts, comments):

    for i, post in enumerate(posts):

        pk = post.get("pk")
        post_in_comments = []
        for comment in comments:
            if comment.get("post_id") == pk:
                post_in_comments.append(comment)
        posts[i]["comments_count"] = len(post_in_comments)

        posts[i]["content"] = tag_content(posts[i]["content"])

    return posts


def tag_content(content):

    words = content.split(" ")
    for i, word in enumerate(words):
        if word.startswith('#'):
            tag = word.replace("#", "")
            link = f"<a href='/tag/{tag}'>{word}</a>"
            words[i] = link

    return " ".join(words)
