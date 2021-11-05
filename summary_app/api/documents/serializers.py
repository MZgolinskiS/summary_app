from flask_restx import fields

from summary_app.api.restx import api

document_text_parser = api.parser()
document_text_parser.add_argument("text", type=str, help="document text", location="form")

document = api.model('Document', {
    "id": fields.Integer(readOnly=True, description="The unique identifier of a document"),
    "text": fields.String(required=True, description="Document content"),
})

summary = api.model('Summary', {
    "id": fields.Integer(readOnly=True, description="The unique identifier of a summary"),
    "document_id": fields.Integer(required=True, description="Document identifier"),
    "summary": fields.String(required=True, description="Summary"),
})
