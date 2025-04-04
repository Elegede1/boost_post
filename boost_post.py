from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, abort
import datetime
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text
# from forms import LoginForm, RegisterForm, PostForm
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import asyncio
from flask_socketio import SocketIO, emit, join_room, leave_room, send
# import websockets

import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
soketio = SocketIO(app)
Bootstrap5(app)




@app.route('/')
def index():
    return render_template("index.html", community=community, aboutus=aboutus, signup=signup, login=login, chat=chat)

@app.route('/community')
def community():
    return render_template("community.html", community=community, aboutus=aboutus, signup=signup, login=login, chat=chat)

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html", community=community, aboutus=aboutus, signup=signup, login=login, chat=chat)

@app.route('/signin')
def login():
    return render_template("signin.html", community=community, aboutus=aboutus, signup=signup, login=login, chat=chat)
@app.route('/signup')
def signup():
    return render_template("signup.html", community=community, aboutus=aboutus, signup=signup, login=login, chat=chat)
@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template("chat.html")

if __name__ == '__main__':
    app.run(debug=True)
    # soketio.run(app, allow_unsafe_werkzeug=True)
