from flask import render_template, redirect, session, url_for
from shop import app, db


@app.route('/')
def home():
    # return render_template('home.html')
    return "Home page of application!"
