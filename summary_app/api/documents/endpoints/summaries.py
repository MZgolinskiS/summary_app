import logging

from flask_restx import Resource

from summary_app.api.documents.endpoints_logic import delete_summary
from summary_app.api.documents.serializers import summary
from summary_app.api.restx import api
from summary_app.database.models import Summary

log = logging.getLogger(__name__)

ns = api.namespace("summaries", description="Operations related to summaries")


@ns.route("/<int:id>")
@api.response(404, "Summary not found.")
class PostItem(Resource):

    @api.marshal_with(summary)
    def get(self, id):
        """
        Returns a summary.
        """
        return Summary.query.filter(Summary.id == id).one()

    @api.response(204, "Summary successfully deleted.")
    def delete(self, id):
        """
        Delete a summary.
        """
        delete_summary(id)
        return None, 204
