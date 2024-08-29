from flask import Flask, request
from flask import render_template
from dotenv import load_dotenv
import os
import json
from post import Post


load_dotenv('config.env')

app = Flask(__name__)

post = Post()

@app.route("/")
def home():   
    print(post.getAllPost())
    return render_template('home.html', context=post.getAllPost())


@app.route("/article/<int:idPost>")
def article(idPost):
        return render_template("article.html", context=post.getPost(idPost))


@app.route("/login")
def login():
    title = request.form["title"]
    password = request.form["password"]
    if title == "admin" and password == "admin":
        return render_template("admin.html")
    else:
        print("error")


@app.route("/new_post", methods=['POST', 'GET'])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        createdAt = request.form["date"]
        content = request.form["content"]
        post.addPost(title, createdAt, content)
        return render_template("home.html")
    return render_template("new_post.html")


@app.route("/edit_post/<int:idPost>", methods=['POST', 'GET'])
def edit_post(idPost):
    if request.method == "POST":
        data = {
        "title": request.form["title"],
        "createdAt": request.form["date"],
        "content": request.form["content"]
        }
        post.updatePost(idPost, data)
        return render_template("home.html")
    print(post.getPost(idPost))
    return render_template("edit_post.html", context = post.getPost(idPost))


if __name__ == '__main__':
    app.run()



