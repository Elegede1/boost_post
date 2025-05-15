from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, abort, session
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
from forms import RegistrationForm, LoginForm, ContactForm, CommunityUploadForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
import secrets
import string



os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Allow HTTP for testing purposes


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
# socketio = SocketIO(app)
Bootstrap5(app)
app.config["GOOGLE_CLIENT_ID"] = os.getenv("GOOGLE_CLIENT_ID")
app.config["GOOGLE_CLIENT_SECRET"] = os.getenv("GOOGLE_CLIENT_SECRET")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")


# Configure Google OAuth
blueprint = make_google_blueprint(
    client_id=app.config["GOOGLE_CLIENT_ID"],
    client_secret=app.config["GOOGLE_CLIENT_SECRET"],
    scope=[
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "openid"
    ],
    redirect_to="google_login_callback",
)
app.register_blueprint(blueprint, url_prefix="/login")


# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader # decorator to load the current user and grab their id
def load_user(user_id):
    # Since the user_id is just the primary key of our user table, use it in the query for the user
    return db.session.get(User, int(user_id))

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    profile_pic: Mapped[str] = mapped_column(String(200))
    is_google_user: Mapped[bool] = mapped_column(Integer, default=0)
    messages: Mapped[list] = relationship("Message", back_populates="user")
    def __repr__(self): # used for debugging
        return f'<User {self.name}>'
    

class Message(db.Model):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))
    content: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime.datetime] = mapped_column(db.DateTime, default=datetime.datetime.utcnow)
    user: Mapped[User] = relationship("User", back_populates="messages")
    def __repr__(self): # used for debugging
        return f'<Message {self.content}>'
    
# Initialize Flask-WTF CSRF protection
csrf = CSRFProtect(app)



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
    # if user is authenticated, show the user profile picture by the 'Qeustion' input
    if current_user.is_authenticated:
        return render_template("community.html", community=community, aboutus=aboutus, signup=signup, login=login, user=current_user)
    else:
        return render_template("community.html", community=community, aboutus=aboutus, signup=signup, login=login)

@app.route('/aboutus')
def aboutus():
    return render_template("about-us.html", community=community, aboutus=aboutus, signup=signup, login=login)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.")
        return redirect(url_for('index'))
    

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
        #     flash('Invalid email or psassword')
    
    return render_template("login.html", login=login)

@app.route('/login/google')
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    return redirect(url_for("google_login"))

@app.route('/login/google/callback')
def google_login_callback():
    if not google.authorized:
        flash("Authentication failed.")
        return redirect(url_for("login"))
    
    resp = google.get("/oauth2/v1/userinfo") # Get user info from Google
    if resp.ok:
        google_info = resp.json()
        email = google_info["email"]
        
        # Check if user exists in your database
        user = User.query.filter_by(email=email).first()
        
        # If user doesn't exist, create a new one
        if not user:
                        # Generate a random password for Google users
            random_password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(20))
            hashed_password = generate_password_hash(random_password)
            user = User(
                email=email,
                name=google_info.get("name", ""),
                profile_pic=google_info.get("picture", ""),
                is_google_user=True,
                password=hashed_password # Store the generated password
            )
            db.session.add(user)
            db.session.commit()
            
        # Log in the user
        login_user(user)
        flash("Successfully logged in with Google!")
        return redirect(url_for("index"))
    
    flash("Failed to get user info from Google.")
    return redirect(url_for("login"))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    registration_form = RegistrationForm
    if request.method == 'POST':
        # Handle regular signup
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered')
            return redirect(url_for('index'))
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        # Log in the new user
        login_user(new_user)
        return redirect(url_for('index'))
    
    return render_template("signup.html", form=registration_form, signup=signup, login=login)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    # Clear the Google OAuth token
    session.clear() # This will clear the session and log out the user
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
    with app.app_context():
        db.create_all()  # Uncomment if you want to create tables
        pass

    app.run(debug=True)
