import requests
import datetime
import json
import pytz

class PyLoki:

	def __init__(self, host: str='localhost', port: str=3100,
				 username: str='', password: str='', protocol: str='http',
				 source: str='default', job='default', src_host='localhost'):

		self._address = f'http://{username}@{password}{host}:{port}'
		self._source = source
		self._host = host
		self._job = job
		self._src_host = src_host
		self._post_address = f'{self._address}/api/prom/push'
		self._tz = 'Asia/Kolkata'
		self._headers = {
    			'Content-type': 'application/json'
		}


	def set_header(self, key: str, value: str):
		self._header[key] = value


	def set_tz(self, zone='Asia/Kolkata'):
		self._tz = zone


	def debug(self, msg):
		payload = self.__message_stream(msg, 'DEBUG')
		return requests.post(self._post_address, data=payload, headers=self._headers)


	def info(self, msg):
		payload = self.__message_stream(msg, 'INFO')
		return requests.post(self._post_address, data=payload, headers=self._headers)


	def warn(self, msg):
		payload = self.__message_stream(msg, 'WARN')
		return requests.post(self._post_address, data=payload, headers=self._headers)


	def critical(self, msg):
		payload = self.__message_stream(msg, 'CRITICAL')
		return requests.post(self._post_address, data=payload, headers=self._headers)


	def __message_stream(self, message, label='INFO') -> str:
		now = datetime.datetime.now(pytz.timezone(self._tz))
		now = now.isoformat('T')
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

