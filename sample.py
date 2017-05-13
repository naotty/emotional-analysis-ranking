#!/usr/bin/python
# _*_ coding: utf-8 _*_

import requests
import os


class Kintone:
    def __init__(self):
        self.url = os.environ['KINTONE_URL']
        self.app_id = os.environ['KINTONE_APP_ID']
        self.api_token = os.environ['KINTONE_API_TOKEN']

    def post(self, username, value):
        data = self.__build_data_params(username, value)
        headers = self.__build_headers()
        resp = requests.post(self.url, json=data, headers=headers)
        return resp

    # private
    def __build_data_params(self, username, value):
        return {
            'app': self.app_id,
            'record': {
                'name': {
                    'value': username,
                },
                'value': {
                    'value': value,
                }
            }
        }

    def __build_headers(self):
        return {
            'Content-Type': 'application/json',
            'X-Cybozu-API-Token': self.api_token,
        }


if __name__ == '__main__':
    kintone = Kintone()
    resp = kintone.post('ishizawa', '200')
    print(resp.text)
