from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year_now = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=year_now)


@app.route('/guess/<name>')
def guess(name):
    # gender_guess = "MF"
    # age_guess = "oops"

    gen_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    gen_response = requests.get(url=gen_url)
    gender_data = gen_response.json()
    age_response = requests.get(url=age_url)
    gender = gender_data["gender"]
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/3cd89f793139e97036a9"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
