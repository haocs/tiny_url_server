from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://tiny_url:tiny1234@localhost/devdb'
db = SQLAlchemy(app)

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_url = db.Column(db.String(255), unique=True)

    def __init__(self, url):
        self.origin_url = url

    def __repr__(self):
        return '<Urls %r>' % self.origin_url

