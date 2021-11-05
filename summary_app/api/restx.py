import logging
import traceback

from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound

from summary_app import settings

log = logging.getLogger(__name__)

api = Api(version="0.0", title="Document analyzer API", description="Simple Flask text document analyzer API.")


@api.errorhandler
def default_error_handler(e):
    message = "Unexpected server error."
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {"message": message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {"message": "The object in the database was not found."}, 404
