from main.models.Operation import Operation


def calc_operation(calc_params: dict) -> dict:
    operation = __params_factory(calc_params)
    result = __calc_operation(operation=operation)

    return {
        "code": 200, "msg": "Calculation Finished!", "data": [{
            "time": "2025-09-10 00:00:00",#round(result, 6)
            "price":1,
            "pv":10,
            "load":100
        }]
    }


def __calc_operation(operation):
    algorithm_mapping = {
        "ARBI":"Arbicharge"
    }

    try:
        operationType = operation.operationType
        algorithm = algorithm_mapping[operationType]

        import_package = "main.algorithms." + algorithm
        algo = __import__(import_package, fromlist = [""])
        result = algo.run(operation)
        return result
    except ImportError as ex:
        return ex


def __params_factory(calc_params):
    operation = Operation()

    if calc_params.__contains__("projectId"):
        operation.proposalId = calc_params["projectId"]

    if calc_params.__contains__("generationTaskId"):
        operation.generationTaskId = calc_params["generationTaskId"]

    if calc_params.__contains__("proposalId"):
        operation.proposalId = calc_params["proposalId"]

    if calc_params.__contains__("taskId"):
        operation.taskId = calc_params["taskId"]

    if calc_params.__contains__("businessId"):
        operation.businessId = calc_params["businessId"]

    if calc_params.__contains__("operationType"):
        operation.operationType = calc_params["operationType"]

    if calc_params.__contains__("revenueName"):
        operation.revenueName = calc_params["revenueName"]

    if calc_params.__contains__("beginTime"):
        operation.beginTime = calc_params["beginTime"]

    if calc_params.__contains__("endTime"):
        operation.endTime = calc_params["endTime"]

    if calc_params.__contains__("batteryCapacity"):
        operation.batteryCapacity = calc_params["batteryCapacity"]

    if calc_params.__contains__("inflation"):
        operation.inflation = calc_params["inflation"]

    if calc_params.__contains__("connectionPointLimitation"):
        operation.connectionPointLimitation = calc_params["connectionPointLimitation"]

    if calc_params.__contains__("interval"):
        operation.interval = calc_params["interval"]

    if calc_params.__contains__("operationType"):
        operation.operationType = calc_params["operationType"]

    if calc_params.__contains__("priceMatrix"):
        operation.priceMatrix = calc_params["priceMatrix"]

    if calc_params.__contains__("priceMatrixData"):
        operation.priceMatrixData = calc_params["priceMatrixData"]

    if calc_params.__contains__("minSOC"):
        operation.minSOC = calc_params["minSOC"]

    if calc_params.__contains__("maxSOC"):
        operation.maxSOC = calc_params["maxSOC"]

    if calc_params.__contains__("costPerUnit"):
        operation.costPerUnit = calc_params["costPerUnit"]

    if calc_params.__contains__("maxChargeDischarge"):
        operation.maxChargeDischarge = calc_params["maxChargeDischarge"]

    if calc_params.__contains__("rte"):
        operation.rte = calc_params["rte"]

    if calc_params.__contains__("strategy"):
        operation.strategy = calc_params["strategy"]
    
    if calc_params.__contains__("unitChargeDischarge"):
        operation.unitChargeDischarge = calc_params["unitChargeDischarge"]

    if calc_params.__contains__("country"):
        operation.country = calc_params["country"]

    if calc_params.__contains__("state"):
        operation.state = calc_params["state"]

    if calc_params.__contains__("market"):
        operation.market = calc_params["market"]

    if calc_params.__contains__("year"):
        operation.year = calc_params["year"]

    return operation
