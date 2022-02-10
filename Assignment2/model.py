from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server import db


class Build(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(256), unique=True, nullable=False)
    repository = db.Column(db.String(256), unique=True, nullable=False)
    owner = db.Column(db.String(256), unique=True, nullable=False)
