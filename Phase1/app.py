"""Flask web application that exposes time and health endpoints."""

import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_time():
    """Return the current server time."""
    now = datetime.datetime.now()
    return f"Current time: {now}", 200

@app.route('/health')
def health():
    """Health check endpoint."""
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
