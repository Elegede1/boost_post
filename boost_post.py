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
# import firebase_admin
# from firebase_admin import credentials, firestore

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
Bootstrap5(app)

# # Initialize Firebase Admin SDK
# # You'll need to download your service account key from Google Cloud Console
# cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
# if not firebase_admin._apps:
#     cred = credentials.Certificate(cred_path)
#     firebase_admin.initialize_app(cred)
#
# # Get Firestore client
# db = firestore.client()

# Example function to save a message to Firestore
def save_message(username, message, timestamp):
# <<<<<<<<<<<<<<  ✨ Codeium Command ⭐ >>>>>>>>>>>>>>>>
    """
    Saves a message to Firestore with the given username, message, and timestamp.

    Args:
        username: str, the username of the person sending the message
        message: str, the message being sent
        timestamp: datetime.datetime, the timestamp of the message

    Returns:
        str, the ID of the message document in Firestore
    """
# <<<<<<<  3104cc8f-4142-4779-8c6e-79ac087f9e04  >>>>>>>
#     message_ref = db.collection('messages').document()
#     message_ref.set({
#         'username': username,
#         'message': message,
#         'timestamp': timestamp
#     })
#     return message_ref.id

# Example function to get messages from Firestore
def get_messages(limit=50):
    messages = db.collection('messages').order_by('timestamp').limit(limit).stream()
    return [message.to_dict() for message in messages]

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
    # Get previous messages from Firestore
    messages = get_messages()
    return render_template("chat.html", messages=messages)

# Socket.IO event handlers
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', 'Connected to server')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

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
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
