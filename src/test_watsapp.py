from unittest import TestCase
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

if 'PATH_TO_ENV' in dotenv_values(".env"):
    load_dotenv(dotenv_path=os.environ.get('PATH_TO_ENV'))
else:
    load_dotenv(dotenv_path='C:\\config_bank_rko\\.env')


from watsapp import *
api_key = os.environ.get('wappi_pro_api_key')
profile_id = os.environ.get('wappi_pro_profile_id')

class WappiProSendMessTestCase(TestCase):
    def test_0(self):
        '''
            {
              "status": "done",
              "timestamp": 1695623834,
              "time": "2023-09-25T09:37:14+03:00",
              "message_id": "3EB05A23842595C201AE9D",
              "task_id": "e09fbdfb-6348-4f15-a3d4-a24c6b1a5765",
              "uuid": "7d4c15ea-3935"
            }

        :return:
        '''

        phone = '79050818476'
        phone = '79582413910'
        mess = '''Здравствуйте!
            По результатам нашего с вами диалога, предоставляем  бесплатный месяц пользования бухгалтеским сервисом.
            Для получения достаточно пройти по указанным ниже ссылкам и оставить заявку на открытие расчётного счёта 
            в одном из банков - партнёров:
            Альфа банк: https://alfa.link/RC9G2g
            Банк Точка: https://partner.tochka.com/fp/?referer1=kckireev'''

        print(WappiProSendMess(profile_id, api_key, mess, phone).get_rezult())


class DevelopTestCase(TestCase):
    def test_0(self):
        l = [1, 4, 'j']
        t = [1, 4, 'j']

        print(hash(tuple(l)))
        print(hash(tuple(t)))


    def test_1(self):
        limit = 100
        offset = 0
        date = '2023-05-02T23:16:58'
        order = 'desc'
        # 1956686116
        print(hash(str(WappiProMessAllGet(profile_id, api_key, limit, offset, date, order).get_rezult())))
