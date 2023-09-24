import os
import sys

from loguru import logger
from flask import request
from flask_restx import Resource

# from main.algorithms.BlackElectricityFAAlgorithm import calc_electricity_with_fixed_amount
# from main.algorithms.BlackElectricityPAAlgorithm import calc_electricity_with_fixed_percentage
from main.service.datatransfer_service import (
    calc_operation,
)

from main.models.operation_vo_model import (
    OperationModel,
    operation_api
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

operationApi = operation_api

@operationApi.route("/transfer")
class Operation(Resource):
    operationRequest = OperationModel.operation_request
    operationResponse = OperationModel.operation_response

    @operationApi.doc("Transfer数据传输-transfer")
    @operationApi.expect(operationRequest)
    @operationApi.response(200, "success", operationResponse)
    def post(self) -> dict:
        """Transfer数据传输-transfer"""
        data = request.json
        try:
            logger.info("transfer 请求参数：" + str(data))
            return calc_operation(data)
        except Exception as ex:
            logger.exception(ex)
            return {"code": 500, "msg": str(ex)}

