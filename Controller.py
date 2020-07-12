from flask import render_template, redirect, url_for, request, json
from App import app
import hashlib

@app.route('/')
def login():
    return render_template('login/login.html')

@app.route('/home')
def home():
    return render_template('home/home.html')

@app.route('/register')
def register():
    return render_template('register/register.html')