from main.repos.Dpdata import Operation_Db
from main.models import ClickHouseSettings

class algorithmBase:
  def __init__(self, beginTime, endTime, interval, priceMatrix, priceMatrixData, generationTaskId, projectId):
        self._operation_repo = Operation_Db()
        self._beginTime = beginTime
        self._endTime = endTime
        self._interval = interval
        self._priceMatrix = priceMatrix
        self._priceMatrixData = priceMatrixData
        self._generationTaskId = generationTaskId
        self._projectId = projectId

  def process_price(self):
        return self._operation_repo.get_price_by_date_interval(self._beginTime, self._endTime,
                                                              self._interval, self._priceMatrix,
                                                              self._priceMatrixData)
  
  def process_load(self):
        return self._operation_repo.get_load_by_date_interval(self._interval, self._projectId)
  
  def get_click_house(self):
        return self._operation_repo.get_generation_data_from_clickhouse(self._generationTaskId)
  
  def save_to_clickhouse(self):
        settings = ClickHouseSettings.ClickHouseSettings()
        CONNECTION = {
            'host': settings.clickhouse_host,
            'database': settings.clickhouse_database_name,
            'user': settings.user,
            'password': settings.password
        }
        return CONNECTION

