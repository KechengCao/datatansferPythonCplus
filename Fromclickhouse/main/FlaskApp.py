import requests
import threading
from flask import Flask
# from main.mq.PushConsumer import start_mq
from loguru import logger


class FlaskApp(Flask):
    def __init__(self, *args, **kwargs):
        super(FlaskApp, self).__init__(*args, **kwargs)
        self._activate_background_job()

    @staticmethod
    def _activate_background_job():
        def run_job():
           # start_mq()
            logger.info("RocketMQ 监听起开启！")

        t1 = threading.Thread(target=run_job)
        t1.start()
