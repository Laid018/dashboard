from flask import render_template, redirect, url_for, request, json
from App import app
import hashlib

# Rutas de la aplicacion
@app.route('/')
def login():
    return render_template('login/login.html')

@app.route('/forgot-password')
def forgot():
    return render_template('forgot/forgot-pass.html')

@app.route('/home')
def home():
    return render_template('home/home.html')

@app.route('/register')
def register():
    return render_template('register/register.html')

@app.route('/register-user')
def register_user():
    return render_template('register/register-admin.html')