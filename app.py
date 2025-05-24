import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use the environment variable set in Render dashboard
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

# Optional: Track modifications warning off
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Example model (optional, for testing DB connection)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

# Example route
@app.route('/')
def home():
    return "Flask app deployed and running!"

# Run locally (not used on Render, only for development)
if __name__ == '__main__':
    app.run(debug=True)


