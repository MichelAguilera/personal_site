from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt as bc # because I can't spell Bcrypt if my life depended on it...


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fake_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Keep !!!!! import routes !!!!! at the end to avoid circular imports.
from psflask import routes