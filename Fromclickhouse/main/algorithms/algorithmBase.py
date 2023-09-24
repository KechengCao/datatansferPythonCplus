from main.repos.Dpdata import Operation_Db
from main.models import ClickHouseSettings

class algorithmBase:
  def __init__(self, start_date, end_date, time_interval, price_matrix, price_matrix_data, generation_task_id):
        self._operation_repo = Operation_Db()
        self._start_date = start_date
        self._end_date = end_date
        self._time_interval = time_interval
        self._price_matrix = price_matrix
        self._price_matrix_data = price_matrix_data
        self._generation_task_id = generation_task_id

  def process(self):
        return self._operation_repo.get_data_by_date_interval(self._start_date, self._end_date,
                                                              self._time_interval, self._price_matrix,
                                                              self._price_matrix_data)
  
  def get_click_house(self):
        return self._operation_repo.get_generation_data_from_clickhouse(self._generation_task_id)
  
  def save_to_clickhouse(self):
        settings = ClickHouseSettings.ClickHouseSettings()
        CONNECTION = {
            'host': settings.clickhouse_host,
            'database': settings.clickhouse_database_name,
            'user': settings.user,
            'password': settings.password
        }
        return CONNECTION

