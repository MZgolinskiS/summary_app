from typing import AnyStr

from summary_app.database import db


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return '<Document %r>' % self.id


class Summary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))
    summary = db.Column(db.Text)

    def __init__(self, document_id: int, text: AnyStr):
        self.document_id = document_id
        self.summary = text

    def __repr__(self):
        return '<Summary %r>' % self.id
