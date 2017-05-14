# _*_ coding: utf-8 _*_

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division
import boto3
import json
import sys
import os
import requests


class Rekognition():
    def __init__(self):
        try:
            self.aws_region = 'us-east-1'
            self.client = boto3.client('rekognition', region_name=self.aws_region)
        except:
            message = "Unexpected error: " + sys.exc_info()[0]
            raise message

    def request(self, s3_bucket, object):
        try:
            response = self.client.detect_faces(
                Image={
                    'S3Object': {
                        'Bucket': s3_bucket,
                        'Name': object
                    }
                },
                Attributes=[
                    'ALL',
                ]
            )
            return response['FaceDetails'][0]['Emotions']
        except:
            return []


class Kintone:
    def __init__(self):
        self.url = os.environ['KINTONE_URL']
        self.app_id = os.environ['KINTONE_APP_ID']
        self.api_token = os.environ['KINTONE_API_TOKEN']

    def post(self, username, type, value):
        data = self.__build_data_params(username, type, value)
        headers = self.__build_headers()
        resp = requests.post(self.url, json=data, headers=headers)
        return resp

    # private
    def __build_data_params(self, username, type, value):
        return {
            'app': self.app_id,
            'record': {
                'name': {
                    'value': username,
                },
                'type': {
                    'value': type,
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


def lambda_handler(event, context):
    # extract
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    object = event['Records'][0]['s3']['object']['key']
    username, ext = os.path.splitext(object)

    # analysis
    rkg = Rekognition()
    response = rkg.request(s3_bucket, object)
    print(json.dumps(response))

    # send to kintone
    kintone = Kintone()
    for r in response:
        resp = kintone.post(username, r['Type'], r['Confidence'])
        print(resp.text)


if __name__ == "__main__":
    json_data = '{"Records": [{"eventVersion": "2.0","eventTime": "2017-05-14T02:14:22.541Z","requestParameters": {"sourceIPAddress": "59.139.177.135"},"s3": {"configurationId": "74eafe6e-1fde-4de4-86bd-e06e4c2bd7d3","object": {"eTag": "0c5afa88b693025960738e913087c969","sequencer": "005917BD7D65DE6C5A","key": "profile.jpg","size": 71077},"bucket": {"arn": "arn:aws:s3:::jawsug-aomori-sample","name": "jawsug-aomori-sample","ownerIdentity": {"principalId": "A3N2PJ4KZ88I7V"}},"s3SchemaVersion": "1.0"},"responseElements": {"x-amz-id-2": "9BZn+q1TSKwLv9S+bvKAb0xx3nQegbOLXlLp58jksfoibartHQEf1koHi3LLTHYASZwj7eQRYI8=","x-amz-request-id": "743079DD6F17D881"},"awsRegion": "us-east-1","eventName": "ObjectCreated:Put","userIdentity": {"principalId": "AWS:AROAJAKSREYC3P7VMRAXO:AWS-CLI-session-1494727512"},"eventSource": "aws:s3"}]}'
    event = json.loads(json_data)
    lambda_handler(event, {})
