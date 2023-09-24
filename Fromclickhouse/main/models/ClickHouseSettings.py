import json


class ClickHouseSettings(object):

    def __init__(self):
        super(ClickHouseSettings, self).__init__()

        try:
            with open('./clickhouse_settings.json', 'r', encoding='utf8') as fp:
                configs_dict = json.load(fp)
                self._entity = configs_dict
        except:
            try:
                with open('Fromclickhouse/main/clickhouse_settings.json', 'r', encoding='utf8') as fp:
                    configs_dict = json.load(fp)
                    self._entity = configs_dict
            except:
                with open('./main/clickhouse_settings.json', 'r', encoding='utf8') as fp:
                    configs_dict = json.load(fp)
                    self._entity = configs_dict

    def __getattribute__(self, key):
        entity = super(ClickHouseSettings, self).__getattribute__("_entity")
        return entity[key]
