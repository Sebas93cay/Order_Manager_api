from flask import Blueprint

api = Blueprint('api', __name__, url_prefix="/api/v1")


def addEndpoints():
    from app.api.v1 import endpoints


addEndpoints()
