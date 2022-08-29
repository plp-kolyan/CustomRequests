from unittest import TestCase
import json
from requests.models import Response
from requests import ConnectionError, HTTPError, get
from src.requestsgarant import RequestsGarant


def get_requestsgarant(args):
    g = Get(**args)
    obj = RequestsGarant()
    obj.get_response_functions = g.get_response_functions
    print(obj.get_rezult())

def get_rezult(functions_wrapper, args):
    functions_wrapper(args)

class Get:
    def __init__(self,
                 status_code = None,
                 err_cls = None,
                 content = None
                 ):

        self.status_code = status_code

        self.err_cls = err_cls

        self.content = content


    def get_response(self):
        response = Response()
        response.status_code = self.status_code
        if self.content is not None:
            try:
                response._content = json.dumps(self.content).encode('utf-8')
            except Exception:
                response._content = self.content.encode('utf-8')
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

        dict(status_code=200, content={'key': 'Привет мир'}),
        dict(status_code=400, content={'key': 'Привет мир'}),
        dict(status_code=200, content='ghjfmtl'),
        dict(status_code=200),
        dict(err_cls=ConnectionError),
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
        string = 'Привет мир'
        bytes_string = string.encode('utf-8')
        print(bytes_string)
        print(bytes_string.decode('utf-8'))

        print(json.dumps(string).encode('utf-8'))

        # dic = json.loads(bytes_string)
        # print(dic)
