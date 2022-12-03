from flask import render_template, url_for, flash, redirect
from psflask import app
from psflask.forms import RegistrationForm, LoginForm
from psflask.models import User, Post

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template('/home.html')

@app.route("/about")
def about():
    return render_template('/about.html')

@app.route("/links")
def links():
    return render_template('/links.html')

@app.route("/gallery")
def gallery():
    return render_template('/gallery.html')

@app.route("/devlog")
def devlog():
    return render_template('/devlog.html')