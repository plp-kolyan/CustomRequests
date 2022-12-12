from requestsgarant import RequestsGarant
from bs4 import BeautifulSoup
import os
import csv


class ParserHidemy(RequestsGarant):

    def __init__(self, params):
        super().__init__()
        self.headers = {'content-type': 'text/plain;charset=UTF-8',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
                        }
        self.params = params
        self.url = 'https://hidemy.name/ru/proxy-list/'
        self.method = 'get'
        self.finish = False

    def do_status_code(self):
        if (soup := BeautifulSoup(self.response.content, 'lxml')) is not None:
            if (table_soup := soup.find("div", class_="table_block")) is not None:
                tr_soup = table_soup.find_all('tr')
                if len(tr_soup) == 1:
                    self.finish = True
                    return f"Последняя таблица"
                elif len(tr_soup) > 1:
                    with open(f'{os.path.abspath(os.curdir)}/{self.__class__.__name__}.csv', 'a', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        for td_soup in tr_soup:
                            self.write_row(writer, td_soup)
                    return f"записываем {len(tr_soup)}"
                else:
                    return f"tr_soup меньше 1: {len(tr_soup)}"

            return f"table_block отсутствует {self.response.text}"
        return f"нет супа {self.response.text}"


    @staticmethod
    def write_row(writer, tr_soup):
        try:
            writer.writerow([tr_soup.text for tr_soup in tr_soup.find_all('td')])
        except Exception as e:
            print(e)




def start_parser_hidemi(params, cls=ParserHidemy):
    for start in range(0, 17000, 64):
        params.update({'start': start})
        obj = cls(params).get_obj_rezult()
        print(f"start={start}, {obj.rezult}")
        if obj.finish:
            return start

