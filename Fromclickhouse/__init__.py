from flask_restx import Api
from flask import Blueprint
from main.controller.operation_controller import (operationApi)

blueprint = Blueprint("datatransfer_api", __name__)
authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    blueprint,
    title="chelion 数据传输",
    version="1.0",
    description="a chelion for flask restplus  web service",
    authorizations=authorizations,
    security="chelion",
)

api.add_namespace(operationApi)