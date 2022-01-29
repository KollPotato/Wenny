from flask import Flask, render_template, url_for, session, redirect, request
from flask_socketio import SocketIO
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json, asyncio, random, hashlib, datetime, requests

app = Flask(__name__)
app.secret_key = 'NbP5?D3SpQd1!'

mysql = MySQL(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('app/index.html')

@app.route('/app', methods=['POST', 'GET'])
def home():
    return render_template('app/home.html')

@app.route('/login')
def login():
    return render_template('app/login.html')

@app.route('/register')
def register():
    return render_template('app/register.html')

@app.route('/profile')
def profile():
    return render_template('app/profile.html')