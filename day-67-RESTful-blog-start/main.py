from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # body = StringField("Blog Content", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # posts = db.session.query(BlogPost).all()
    # requested_post = None
    # for blog_post in posts:
    #     if blog_post["id"] == post_id:
    #         requested_post = blog_post
    # return render_template("post.html", post=requested_post)
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    new_form = CreatePostForm()
    if new_form.validate_on_submit():
        now = datetime.now()
        add_new_post = BlogPost(
            title=new_form.title.data,
            subtitle=new_form.subtitle.data,
            date=now.strftime("B% %d, %Y"),
            body=new_form.body.data,
            author=new_form.author.data,
            img_url=new_form.img_url.data,
        )
        db.session.add(add_new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=new_form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=requested_post.title,
        subtitle=requested_post.subtitle,
        img_url=requested_post.img_url,
        author=requested_post.author,
        body=requested_post.body,
    )
    if edit_form.validate_on_submit():
        requested_post.title=edit_form.title.data
        requested_post.subtitle=edit_form.subtitle.data
        requested_post.img_url=edit_form.img_url.data
        requested_post.author=edit_form.author.data
        requested_post.body=edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=requested_post.id))
    else:
        return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
def delete(post_id):
    post_to_be_deleted = BlogPost.query.get(post_id)
    db.session.delete(post_to_be_deleted)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
