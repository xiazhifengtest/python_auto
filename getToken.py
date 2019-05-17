import requests
import unittest
import json


def getToken():
    url = 'https://yk.xox5.com/yk/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    data = {'username': 'mayanju', 'password': '031064'}
    res = requests.post(url=url, data=data, headers=headers)
    return res.json()['data']['token']



