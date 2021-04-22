from src import app
from flask import render_template, request, redirect, url_for, session 
import string
import random


@app.route('/')
def index():
    if "user" in session:
        return redirect(url_for('user'))
    return render_template('index.html')
