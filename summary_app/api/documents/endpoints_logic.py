from typing import AnyStr

from sqlalchemy.exc import MultipleResultsFound

from summary_app.database import db
from summary_app.database.models import Document, Summary
from summary_app.text_analyzer.text_analyzer import TextAnalyzerInstance


def create_document(text: AnyStr) -> Document:
    document = Document(text)
    db.session.add(document)
    db.session.commit()
    return document


def update_document(document_id: int, text: AnyStr):
    document = Document.query.filter(Document.id == document_id).one()
    document.text = text
    db.session.add(document)
    db.session.commit()


def delete_document(document_id: int):
    document = Document.query.filter(Document.id == document_id).one()
    db.session.delete(document)
    db.session.commit()


def create_summary(document_id: int) -> Summary:
    summary = list(Summary.query.filter(Summary.document_id == id))
    if len(summary) == 1:
        return summary[0]
    if len(summary) > 1:
        raise MultipleResultsFound(f"Multiple summaries found for the document id: {id}")
    document = Document.query.filter(Document.id == id).one()
    summary_dict = TextAnalyzerInstance.summarization_as_dict(document.text)
    summary = Summary(document_id, summary_dict)
    db.session.add(summary)
    db.session.commit()
    return summary


def update_summary(document_id: int, summary_json: AnyStr):
    summary = Summary.query.filter(Summary.document_id == document_id).one()
    summary.summary = summary_json
    db.session.add(summary)
    db.session.commit()


def delete_summary(id: int):
    summary = Summary.query.filter(Summary.id == id).one()
    db.session.delete(summary)
    db.session.commit()
