from time import time
from server import db
from dataclasses import dataclass


@dataclass
class Build(db.Model):
    id: int
    repo_name: str
    owner: str
    pusher: str
    branch: str
    repo_name: str
    timestamp: int
    syntax_result: bool

    id = db.Column(db.Integer, primary_key=True)
    repo_name = db.Column(db.String(256), nullable=False)
    owner = db.Column(db.String(256), nullable=False)
    pusher = db.Column(db.String(256), nullable=False)
    branch = db.Column(db.String(256), nullable=False)
    repo_url = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(db.Integer())
    syntax_result = db.Column(db.Boolean)
