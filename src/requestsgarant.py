import time

import requests
import traceback


def return_test_response(json_data: dict, status_code: int = 200):
    import json
    from requests.models import Response
    the_response = Response()
    the_response.code = "expired"
    the_response.error_type = "expired"
    the_response.status_code = status_code
    the_response._content = json.dumps(json_data).encode('utf-8')
    return the_response


class RequestsGarant:
    """Кастомная библиотека для запросов"""

    def __init__(self):
        self.success = False
        self.rezult = None
        self.custom_test = False
        self.json = None
        self.data = None
        self.timeout = 50
        self.resend_send = False

        self.connection_error = False
        self.timeot_error = False

    def get_guarantee_response(self):
        try:
            return self.get_response_functions()()
        except requests.exceptions.Timeout:
            self.timeot_error = True
            self.resend_send = True
            return f"Превышен таймаут {self.timeout}"
        except requests.exceptions.ConnectionError:
            self.resend_send = True
            self.connection_error = True
            return "Ошибка подключения"
        except:
            return traceback.format_exc()

    def do_json(self):
        pass

    def do_status_code(self):
        if self.response_status_code == 429:
            self.resend_send = True
            time.sleep(10)
        return self.response_status_code

    def rezult_function(self):
        pass

    def set_null_attr(self, *args_init):
        # обнуление атрибутов
        for attr in [attr for attr in self.__dict__.keys()]:
            args = (self, attr)
            if hasattr(*args):
                delattr(*args)
        self.__init__(*args_init)

    def get_rezult(self):
        self.response = self.get_guarantee_response()
        if type(self.response) is type(requests.models.Response()):
            try:
                self.response_json = self.response.json()
                do_json = self.do_json()
                if do_json is not None:
                    self.rezult = do_json
                    return do_json
                else:
                    self.rezult = self.response_json
                    return self.response_json
            except:
                self.response_status_code = self.response.status_code
                do_status_code = self.do_status_code()
                if do_status_code is None:
                    self.rezult = self.response_status_code
                else:
                    self.rezult = do_status_code
                return do_status_code
        else:
            self.rezult = self.response
            return self.response

    def get_obj_rezult(self):
        self.get_rezult()
        return self

    def return_test_response(self):
        self.define_json_response_test()
        return return_test_response(self.json_response_test)

    def define_json_response_test(self):
        self.json_response_test = {"mess": 'заглушка'}

    def get_response_functions(self):
        self.args_request = {attr: getattr(self, attr) for attr in
                             ['method', 'params', 'url', 'proxies', 'data', 'json', 'headers', 'timeout', 'files', 'verify', 'cert']
                             if hasattr(self, attr) is True and getattr(self, attr) is not None
                             if getattr(self, 'method') == 'get' and attr != 'json'
                             or
                             getattr(self, 'method') == 'post' and attr != 'params'}

        if (self.custom_test and self.test) is True:
            return self.return_test_response
        else:
            return self.get_response_production

    def get_response_production(self):
        return requests.request(**self.args_request)


class RequestsGarantSession(RequestsGarant):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def get_response_production(self):
        return self.session.request(**self.args_request)

class RequestsGarantTest(RequestsGarant):
    def __init__(self):
        super().__init__()

    def get_response_functions(self):
        if self.test is True:
            self.assign_test()
        else:
            self.assign_production()

        return super().get_response_functions()


class RequestsGarantTestBaseUrl(RequestsGarantTest):
    def __init__(self):
        super().__init__()

    def assign_test(self):
        self.url = f"{self.base_url_test}{self.endpoint}"

    def assign_production(self):
        self.url = f"{self.base_url}{self.endpoint}"


def assign_url_endpoint(obj_cuctom_request):
    if obj_cuctom_request.test is True:
        obj_cuctom_request.url = f"{obj_cuctom_request.url}{obj_cuctom_request.test_endpoint}"
    else:
        obj_cuctom_request.url = f"{obj_cuctom_request.url}{obj_cuctom_request.endpoint}"


class RequestsGarantTestEndpoint(RequestsGarantTest):
    def __init__(self):
        super().__init__()

    def assign_test(self):
        self.url = f"{self.base_url}{self.endpoint_test}"

    def assign_production(self):
        self.url = f"{self.base_url}{self.endpoint}"


class RequestsGarantTestHeaders(RequestsGarantTest):
    def __init__(self):
        super().__init__()

    def assign_test(self):
        self.headers.update(self.dict_key_test)

    def assign_production(self):
        self.headers.update(self.dict_key)


class RequestsGarantTestJson(RequestsGarantTest):
    pass
















