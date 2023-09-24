from main.algorithms.algorithmBase import algorithmBase
import numpy as np
import pandas as pd


def main():
    pass

def run(operation) -> int:#pd.DataFrame:
    beginTime = operation.beginTime
    endTime = operation.endTime
    interval = operation.interval
    priceMatrix = operation.priceMatrix
    priceMatrixData = operation.priceMatrixData
    generationTaskId = operation.generationTaskId
    projectId = operation.projectId

    tmp = 0

    data = algorithmBase(beginTime, endTime, interval, priceMatrix, priceMatrixData, generationTaskId, projectId)
    generation_data = data.get_click_house()
    price, base_date = data.process_price()
    load, base_date = data.process_load()



    print(generation_data)


    return tmp