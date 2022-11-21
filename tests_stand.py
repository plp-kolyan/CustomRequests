# coding : utf-8
# PEP-8

import time

from unittest import TestCase
import json
from requests.models import Response
from requests import ConnectionError, HTTPError, get
from src.requestsgarant import RequestsGarant
from loguru import logger


def check_time(func):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        func(*args, **kwargs)
        return logger.info(time.monotonic() - start)

    return wrapper


def get_requestsgarant(args):
    g = Get(**args)
    obj = RequestsGarant()
    obj.get_response_functions = g.get_response_functions
    print(obj.get_rezult())


def get_rezult(functions_wrapper, args):
    functions_wrapper(args)


class Get:
    def __init__(self,
                 status_code=None,
                 err_cls=None,
                 content=None
                 ):

        self.status_code = status_code

        self.err_cls = err_cls

        self.content = content

    def get_response(self):
        response = Response()
        response.status_code = self.status_code
        if isinstance(self.content, dict):
            response._content = json.dumps(self.content).encode('utf-8')
        elif self.content is not None:
            # response._content = self.content.encode('utf-8')
            response._content = self.content

        return response

    def get_trace(self):
        raise self.err_cls

    def get_response_functions(self):
        if self.err_cls is None:
            return self.get_response
        else:
            return self.get_trace


class TestTestCase(TestCase):
    args_list = [


        dict(status_code=200, content={'key': 'hello'}),
        dict(status_code=400, content={'key': 'hello'}),
        dict(status_code=200, content='ghjfmtl'),
        dict(status_code=200),
        # dict(err_cls=ConnectionError),
        dict(err_cls=HTTPError)

    ]

    def test_get_requestsgarant(self):

        for args in self.args_list:
            with self.subTest(args=args):
                get_rezult(get_requestsgarant, args)

    def test_iter_rows(self):
        r = get('https://httpbin.org/stream/20', stream=True)

        if r.encoding is None:
            r.encoding = 'utf-8'

        print(r.content)

        for line in r.iter_lines(decode_unicode=True):
            if line:
                print(json.loads(line))

    def test_0(self):
        string = 'привет мир'
        bytes_string = string.encode('utf-8')
        print(bytes_string)
        print(bytes_string.decode('utf-8'))

        print(json.dumps(string).encode('utf-8'))

        # dic = json.loads(bytes_string)
        # print(dic)

    def test_2(self):
        # invalid bullshit
        content = b'{"title": "Homecredit Bank: \xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0 \xd1\x80\xd0\xb0\xd1\x81\xd1\x81\xd1\x80\xd0\xbe\xd1\x87\xd0\xba\xd0\xb8 \xd0\xa1\xd0\xb2\xd0\xbe\xd0\xb1\xd0\xbe\xd0\xb4\xd0\xb0 (\xd0\xbd\xd0\xb5 \xd0\xb0\xd0\xba\xd1\x82\xd1\x83\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe)"}'
        dec_content = content.decode()
        print(f'writer in log {dec_content}'.encode('utf8'))
        dict_content = json.loads(dec_content)
        print(type(dict_content))

    def test_3(self):
        R = '₽'.lower()
        print(R.encode('utf-16'))

    def test_4(self):
        import requests
        import traceback

        sucsess = False

        try:
            r = requests.post('https://httpbin.org/post', data={'key': 'value'})
        except Exception:
            rezult = traceback.format_exc()

        else:
            try:
                response_json = r.json()
            except:
                response_json = None

            if response_json is not None:
                if 'form' in response_json:
                    rezult = response_json['form']
                    sucsess = True
                else:
                    rezult = response_json
            else:
                rezult = f'status_code: "{r.status_code}", text {r.text}'




        print(rezult)
        print(sucsess)

    def test_5(self):
        import requests

        r = requests.post('https://httpbin.org/post', data={'key': 'value'})
        print(r.json())

    def test_6(self):

