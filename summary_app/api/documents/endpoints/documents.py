import logging

from flask import request
from flask_restx import Resource

from summary_app.api.documents.endpoints_logic import create_document, update_document, delete_document, create_summary
from summary_app.api.documents.serializers import document, document_text_parser, summary
from summary_app.api.restx import api
from summary_app.database.models import Document

log = logging.getLogger(__name__)

ns = api.namespace("documents", description="Operations related to documents")


@ns.route("/")
@api.response(404, "Document not found.")
class PostItem(Resource):

    @api.expect(document_text_parser)
    @api.marshal_with(document)
    def post(self):
        """
        Create a document.
        """
        text = request.form["text"]
        return create_document(text)


@ns.route("/<int:id>")
@api.response(404, "Document not found.")
class PostItem(Resource):

    @api.marshal_with(document)
    def get(self, id):
        """
        Returns a document.
        """
        return Document.query.filter(Document.id == id).one()

    @api.expect(document_text_parser)
    @api.response(204, "Document successfully updated.")
    def put(self, id):
        """
        Updates a document.
        """
        text = request.form["text"]
        update_document(id, text)
        return None, 204

    @api.response(204, "Document successfully deleted.")
    def delete(self, id):
        """
        Deletes document.
        """
        delete_document(id)
        return None, 204


@ns.route("/<int:id>/summary")
@api.response(404, "Document not found.")
class PostItem(Resource):

    @api.marshal_with(summary)
    def get(self, id):
        """
        Creating and returning a document summary, if the summary already exists, it returns it.
        """
        return create_summary(id)
