import requests
import json
import pandas as pd
import numpy as np
import datetime
import pandahouse as house
import main.models.ClickHouseSettings as ClickHouseSettings

settings = ClickHouseSettings.ClickHouseSettings()
CONNECTION = {
    'host': settings.clickhouse_host,
    'database': settings.clickhouse_database_name,
    'user': settings.user,
    'password': settings.password
}


class Operation_Db:

    # 这个地方的api_addr应该去读配置项，不是直接传进来
    def __init__(self) -> None:
        # url的前缀要配置
        self._api_addr_pricematrix = "http://192.168.3.228:30035/service/proposal/operation/queryMatrixPrice"
        self._api_addr_load = "http://192.168.3.241:30035/service/project/load/getByProjectId"
        self._api_addr_dpresult = ""
        # self._api_addr = (
        #         "http://" + api_addr
        # )  # "http://192.168.1.247:30023/facade/device/data/v2/getDeviceData"
        self._headers = {"Content-Type": "application/json", "Accept": "*/*"}

    def get_price_by_date_interval(self, beginTime, endTime, interval, priceMatrix, priceMatrixData):

        url = self._api_addr_pricematrix
        if priceMatrix == "1":
            data = {"model": {"endDate": endTime, "field": 0, "startDate": beginTime,
                              "timeInterval": interval}}

            res = requests.post(url, data=json.dumps(data), headers=self._headers)
            result = res.json()
        else:
            data = {"model": {"endDate": endTime, "field": priceMatrixData, "startDate": beginTime,
                              "timeInterval": interval}}
            res = requests.post(url, data=json.dumps(data), headers=self._headers)
            result = res.json()

        price = []
        closest_date = datetime.datetime.strptime(result["data"][0]["timestamp"], "%Y-%m-%d %H:%M:%S")

        for data in result["data"]:
            price.append(data["price"])
        price_array = np.array(price)

        return price_array, closest_date
    

    def get_load_by_date_interval(self, interval, projectId):
        url = self._api_addr_load
        data = {"model": {"interval": interval, "projectId":projectId}}
        res = requests.post(url, data=json.dumps(data), headers=self._headers)
        result = res.json()

        load = []
        closest_date = datetime.datetime.strptime(result["data"][0]["date"], "%Y-%m-%d %H:%M:%S")

        for data in result["data"]:
            load.append(data["load"])
        price_array = np.array(load)

        return price_array, closest_date


    def get_generation_data_from_clickhouse(self, generation_task_id):

        """generation_task_id用来取generation的中间数据的id"""
        if generation_task_id is None:
            raise Exception("Generation task id cannot be empty while calculate operation.")

        sql = '''SELECT TaskId,Year,Month,Day,Hour,Minute,
            PreGeneration,
            PostDegradeGeneration
            FROM chelion.KoalaCalcResult where TaskId = \'{task_id}\''''\
        .format(task_id=generation_task_id)
        df = house.read_clickhouse(sql, connection=CONNECTION)
        generation_data = list(df["PostDegradeGeneration"])
        return generation_data

        # data = pd.read_csv(file_name)
        # return data.reset_index()

        # df = pd.json_normalize(result["data"]).sort_values(
        #     by=["year", "month", "day", "hour", "minute"], ascending=True
        # )
        # grouped_df = df.groupby(["month", "day", "hour"])[
        #     "DHI", "GHI", "solarZenithAngle", 'windSpeed', 'temperature'
        # ].mean()
        #
        # return grouped_df.reset_index()
