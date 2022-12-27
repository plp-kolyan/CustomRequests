from unittest import TestCase
from requests.models import Response
import os
from src.parserproxy import *
import json

def get_requestsgarant_ob(page_html, requestsgarant_ob):
    requestsgarant_ob.response = Response()
    with open(f'{os.path.abspath(os.curdir)}\\pages\\{page_html}', 'rb') as file:
        requestsgarant_ob.response._content = file.read()
    return requestsgarant_ob

#
# def get_response_content_hidemy_from_file():
#     ph = ParserHidemy({'type': 'h'})
#     pass

class TestTestCase(TestCase):

    def test_get_requestsgarant_ob(self):
        '''
        тест на get_requestsgarant_ob
        :return:
        '''
        requestsgarant_ob = get_requestsgarant_ob('hidemy.name_64_proxy.html', ParserHidemy({}))
        print(requestsgarant_ob.response.content)

    def test_0(self):
        for start in range(0, 15000, 64):
            print({"start": start})

    def test(self):
        start_parser_hidemi({'type': 'h'})

    def test_1(self):
        with open(f'{os.path.abspath(os.curdir)}\\pages\\{"hidemy.name_64_proxy.html"}', 'rb') as file:

            if (soup := BeautifulSoup(file.read(), 'lxml')) is not None:
                if (table_soup := soup.find("div", class_="table_block")) is not None:
                    tr_soup = table_soup.find_all('tr')
                    if len(tr_soup) == 1:
                        return f"Последняя таблица"
                    elif len(tr_soup) > 1:

                            for td_soup in tr_soup:
                                print(td_soup)


class ParserHidemyTestCase(TestCase):
    @staticmethod
    def write_row(writer, tr_soup):
        print([tr_soup.text for tr_soup in tr_soup.find_all('td')])


    def get_ob_parser_hidemy(self, page_html):
        requestsgarant_ob = get_requestsgarant_ob(page_html, ParserHidemy({}))
        requestsgarant_ob.write_row = self.write_row
        return requestsgarant_ob

    def test_hidemy_name_64_proxy(self):
        ob = self.get_ob_parser_hidemy('hidemy.name_64_proxy.html')

        print(ob.do_status_code())
        print(ob.finish)


    def test_hidemy_name_0_proxy(self):
        ob = self.get_ob_parser_hidemy('hidemy.name_0_proxy.html')
        print(ob.do_status_code())
        print(ob.finish)


    def test_ParserHidemy(self):
        ob = ParserHidemy({'type': 'h'})
        ob.write_row = self.write_row
        print(ob.get_rezult())


class HidemyApiTestCase(TestCase):
    def setUp(self) -> None:
        from dotenv import load_dotenv, dotenv_values

        load_dotenv()

        if 'PATH_TO_ENV' in dotenv_values(".env"):
            load_dotenv(dotenv_path=os.environ.get('PATH_TO_ENV'))
        else:
            load_dotenv(dotenv_path='C:\\config_bank_rko\\.env')

        self.code = os.environ.get('hidemy')

    def test_0(self):

        obj = HidemyApi({'out': 'js', 'code': self.code, 'type': 'h'})
        obj.get_obj_rezult()
        print(obj.response)
        with open('HidemyApi.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(obj.response_json))


    def test_1(self):
        with open('HidemyApi.json', 'r', encoding='utf-8') as file:
            print(json.loads(file.read())[0])









