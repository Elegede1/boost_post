from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, abort
import datetime
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import SocketIO, emit, join_room, leave_room, send
import os
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound
import json


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
# socketio = SocketIO(app)
# Bootstrap5(app)



# db = pass

# Example function to save a message to Firestore

#     message_ref = db.collection('messages').document()
#     message_ref.set({
#         'username': username,
#         'message': message,
#         'timestamp': timestamp
#     })
#     return message_ref.id

# def get_messages(limit=50):
#     messages = db.collection('messages').order_by('timestamp').limit(limit).stream()
#     return [message.to_dict() for message in messages]

@app.route('/')
def index():
    return render_template("index.html", community=community, aboutus=aboutus, signup=signup, login=login)

@app.route('/community')
def community():
    return render_template("community.html", community=community, aboutus=aboutus, signup=signup, login=login)

@app.route('/aboutus')
def aboutus():
    return render_template("about-us.html", community=community, aboutus=aboutus, signup=signup, login=login)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle regular login
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Find user by email and verify password
        # user = User.query.filter_by(email=email).first()
        # if user and check_password_hash(user.password, password):
        #     login_user(user)
        #     return redirect(url_for('index'))
        # else:
        #     flash('Invalid email or password')
    
    return render_template("login.html", community=community, aboutus=aboutus, signup=signup, login=login)

@app.route('/login/google')
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    return redirect(url_for("google_login_callback"))

@app.route('/login/google/callback')
def google_login_callback():
    if not google.authorized:
        flash("Authentication failed.")
        return redirect(url_for("login"))
    
    resp = google.get("/oauth2/v1/userinfo")
    if resp.ok:
        google_info = resp.json()
        email = google_info["email"]
        
        # Check if user exists in your database
        # user = User.query.filter_by(email=email).first()
        
        # If user doesn't exist, create a new one
        # if not user:
        #     user = User(
        #         email=email,
        #         name=google_info.get("name", ""),
        #         profile_pic=google_info.get("picture", ""),
        #         is_google_user=True
        #     )
        #     db.session.add(user)
        #     db.session.commit()
        
        # Log in the user
        # login_user(user)
        flash("Successfully logged in with Google!")
        return redirect(url_for("index"))
    
    flash("Failed to get user info from Google.")
    return redirect(url_for("login"))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle regular signup
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if user already exists
        # existing_user = User.query.filter_by(email=email).first()
        # if existing_user:
        #     flash('Email already registered')
        #     return redirect(url_for('signup'))
        
        # Create new user
        # hashed_password = generate_password_hash(password)
        # new_user = User(name=name, email=email, password=hashed_password)
        # db.session.add(new_user)
        # db.session.commit()
        
        # Log in the new user
        # login_user(new_user)
        # return redirect(url_for('index'))
    
    return render_template("signup.html", community=community, aboutus=aboutus, signup=signup, login=login)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    # Clear the Google OAuth token
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('index'))

@app.route('/contact')
def contact():
    return render_template("contact.html")

# @app.route('/chat', methods=['GET', 'POST'])
# def chat():
#     # Get previous messages from Firestore
#     messages = get_messages()
#     return render_template("chat.html", messages=messages)
#
# # Socket.IO event handlers
# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')
#     emit('message', 'Connected to server')
#
# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')

# @socketio.on('message')
# def handle_message(data):
#     print('Received message:', data)
#     # Save message to Firestore
#     if isinstance(data, dict) and 'username' in data and 'message' in data:
#         message_id = save_message(
#             username=data['username'],
#             message=data['message'],
#             # timestamp=firestore.SERVER_TIMESTAMP
#         )
#         data['id'] = message_id
#     # Broadcast the message to all connected clients
#     emit('message', data, broadcast=True)

if __name__ == '__main__':
    # socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
    app.run(debug=True)
