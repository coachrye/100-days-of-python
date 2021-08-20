from flask import Flask, render_template
import requests

# blog_url = "https://api.npoint.io/daf8714af94a00a38c68"
# response = requests.get(blog_url)
# all_posts = response.json()

all_posts = requests.get("https://api.npoint.io/daf8714af94a00a38c68").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
