#!/usr/bin/python3
# @Time    : 2023-08-22
# @Author  : Kevin Kong (kfx2007@163.com)

from hashlib import md5
import json
import requests
import base64

SANDBOX_URL = "https://syncdata-dev.azurewebsites.net"
URL = ""


class Comm(object):

    def __get__(self, instance, owner):
        self._appid = instance._appid
        self._appkey = instance._appkey
        self._sandbox = instance._sandbox
        return self

    def sign(self, data):
        """
        sign before request.

        :param data: request body.
        :return sign: the result of signature
        """

        data = json.dumps(data, separators=(',', ":"))

        raw = f"{self._appid}{data}{self._appkey}"
        print(raw)
        return md5(raw.encode('utf-8')).hexdigest().upper()

    def get_headers(self, data):
        """
        get request header.
        """
        return {
            "appid": self._appid,
            "sign": self.sign(data),
            "appkey": self._appkey
        }

    def format_data(self,data):
        new_data = {}
        for key, value in data.items():
            if value is not None:
                if isinstance(value, dict):
                    new_data.update(self.format_data(value))
                elif  isinstance(value, list):
                    new_data[key] = [self.format_data(item) for item in value]
                else:
                    new_data[key] = value
        return new_data

        isinstance()
                

    def post(self, endpoint, code, data):
        data = self.format_data(data)
        url = f"{SANDBOX_URL if self._sandbox else URL}/api/{endpoint}?code={code}"
        print(url)
        headers = self.get_headers(data)
        raw_data = json.dumps({
            "header": headers,
            "body":data
        })
        base64_data = base64.b64encode(raw_data.encode('utf-8'))
        print('====')
        print(raw_data)
        print(requests.post(url, json={'data': base64_data}).content)
        return requests.post(url, json={'data': base64_data}).json()
 