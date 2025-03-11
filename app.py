from flask import Flask, render_template, redirect, request
from flask_session import Session
import sqlite3
from datetime import timedelta

app = Flask(__name__)



app.secret_key = ''
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/sessions'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=90)



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)