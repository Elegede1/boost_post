# wsgi.py
from boost_post import app, soketio  # Import your Flask app and SocketIO instance

if __name__ == "__main__":
    socketio.run(app)