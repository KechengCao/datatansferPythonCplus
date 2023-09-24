from flask_restx import Namespace, fields

operation_api = Namespace("datatransfer", description="Transfer 数据传输")


class OperationModel:

    operation_request = operation_api.model(
        "Transfer_model",
        {
            "projectId": fields.Integer(
                default=1, required=True, description="projectId"
            ),

            "taskId": fields.String(
                default="1", required=True, description="taskId"
            ),

           "generationTaskId": fields.String(
                default="1", required=True, description="generationTaskId"
            ),

           "proposalId": fields.Integer(
                default=1, required=True, description="proposalId"
            ),

           "businessId": fields.String(
                default="1", required=True, description="businessId"
            ),

            "operationType": fields.String(default="ARBI", required=True, description="operationType"),

            "revenueName": fields.String(default="Arbicharge revenue", required=True, description="revenueName"),

            "beginTime": fields.String(default=1, required=True, description="beginTime"),

            "endTime": fields.String(default=2, required=True, description="endTime"),

            "interval": fields.String(default="5", required=True, description="interval"),

            "connectionPointLimitation": fields.Float(default=1, required=True, description="connectionPointLimitation"),

            "costPerUnit": fields.Float(default=0.2, required=True, description="costPerUnit"),

            "batteryCapacity": fields.Float(default=0.3, required=True, description="batteryCapacity"),

            "inflation": fields.Float(default=0, required=True, description="inflation"),

            "maxChargeDischarge": fields.Float(default=0.01, required=True, description="maxChargeDischarge"),
            
            "maxSOC": fields.Float(default=0, required=True, description="maxSOC"),

            "minSOC": fields.Float(default=100, required=True, description="minSOC"),

            "rte": fields.Float(default=0.01, required=True, description="rte"),

            "strategy": fields.Float(default=1, required=True, description="strategy"),

            "unitChargeDischarge": fields.Float(default=0.01, required=True, description="unitChargeDischarge"),

            "priceMatrix": fields.String(default=2, required=True, description="priceMatrix"),

            "priceMatrixData": fields.Integer(
                default=1, required=True, description="priceMatrixData"
            ),

            "country": fields.String(default="1", required=True, description="country"),           

            "state": fields.String(default="1", required=True, description="state"),     

            "market": fields.String(default="1", required=True, description="market"), 

            "year": fields.Integer(default=1, required=True, description="inter"),
        }

    )

    operation_response = operation_api.model(
        "operation_response",
        {
            "code": fields.String(default="200", description="状态码"),
            "data": fields.List(fields.Nested(
                operation_api.model("data", {
                    "time": fields.String(default="1", required=True, description="time"),
                    "price": fields.Float(default=0.2, required=True, description="price"),
                    "pv": fields.Float(default=0.2, required=True, description="pv"),
                    "load": fields.Float(default=0.2, required=True, description="load")
                }))
            ),
            "msg": fields.String(description="提示"),
        },
    )

