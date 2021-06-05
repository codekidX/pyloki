import json
import datetime
import pytz
import requests
import urllib

from typing import Dict
from requests.models import Response

API_VERSION = 'v1'


class PyLokiClient:
    """
            An early access(alpha) client embedded with this library, Using the client you can query the
            Graphana Loki instance for the logs.
    """

    def __init__(self, address, job: str, source: str) -> None:
        self.__address = address
        self.__job = job
        self.__source = source

    def logs_since(self, time: datetime.datetime, limit: int = 30) -> Response:
        now_stamp = datetime.datetime.now().timestamp
        query = {
            'end': now_stamp * 1000,
            'direction': 'BACKWARD',
            'start': time.timestamp * 1000,
            'query': f'{{job="{self.__job}"}}',
            'limit': limit
        }
        enc_query = urllib.urlencode(query)
        url = f'{self.__address}/loki/api/{API_VERSION}/query_range?{enc_query}'
        return requests.get(url)


class PyLoki:
    """
        PyLoki helps you log your messages in an imperative way with instance initialization.
        Your service can have your own initialized instance and job and log it with your label.
    """

    def __init__(self, host: str = 'localhost', port: str = 3100,
                 username: str = '', password: str = '', protocol: str = 'http',
                 source: str = 'default', job='default', src_host='localhost'):

        if username != '' and password != '':
            self._address = f'http://{username}@{password}{host}:{port}'
        else:
            self._address = f'http://{host}:{port}'

        self._source = source
        self._host = host
        self._job = job
        self._src_host = src_host
        self._post_address = f'{self._address}/api/prom/push'
        self._tz = 'Asia/Kolkata'
        self._headers = {
            'Content-type': 'application/json'
        }
        self.client = PyLokiClient(
            self._address, job=self._job, source=self._source)

    def set_header(self, key: str, value: str):
        self._header[key] = value

    def set_tz(self, zone='Asia/Kolkata'):
        self._tz = zone

    def debug(self, msg) -> Response:
        payload = self.__log_stream(msg, 'DEBUG')
        return requests.post(self._post_address, data=payload, headers=self._headers)

    def info(self, msg) -> Response:
        payload = self.__log_stream(msg, 'INFO')
        return requests.post(self._post_address, data=payload, headers=self._headers)

    def warn(self, msg) -> Response:
        payload = self.__log_stream(msg, 'WARN')
        return requests.post(self._post_address, data=payload, headers=self._headers)

    def critical(self, msg) -> Response:
        payload = self.__log_stream(msg, 'CRITICAL')
        return requests.post(self._post_address, data=payload, headers=self._headers)

    def __log_stream(self, message, label='INFO') -> str:
        tznow = datetime.datetime.now(pytz.timezone(self._tz))
        now = tznow.isoformat('T')
        data = {
            'streams': [
                {
                    'labels': f'{{source="{self._source}",job="{self._job}",host="\'{self._src_host}\'"}}',
                    'entries': [
                        {
                              'ts': now,
                              'line': f'[{label}] {message}'
                        }
                    ]
                }
            ]
        }

        return json.dumps(data)
