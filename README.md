# Garant Success Requests


[Домашняя страница](https://github.com/plp-kolyan/CustomRequests.git)

Даннная библиотека позволяет легко обходить стандартные ограничение библиотеки requests
например:
- В случае сбоя декодирования JSON requests.json() возникает исключение.
- Когда отсутствует интернет requests поднимает исключение
- Помогает создавать тестовые заглушки

Установить
>pip install garant_success_requests

Минимальный пример:
    
    from requestsgarant import RequestsGarant

    class YandexRequest(ResponseGarant):
        def __init__(self):
            super().__init__()
            self.method = 'get'
            self.url = 'https://ya.ru/'

    print(YandexRequest().get_rezult())
    
>ответ 200
    
Документация:
По умолчанию метод get_rezult возвращает результат выполнения метода do_json который вернет dict c
ответом сервера, в случае сбоя декодирования ответа вернет результат метода do_status_code, который
вернет статус код ответа сервера int, если при взятии запроса возникнет исключение то результатом будет
текст исключения.
Сам результат записывается в атрибут rezult, поэтому чтобы получить результат

В примере выше мы уже получили ответ в которм отработал метод do_status_code, но очевидно что нас не
устраивает получение только одного кода, поэтому поэтому надо переопределить метод do_status_code
    from garant_success_requests.custom_requests import ResponseGarant

    from garant_success_requests.custom_requests import ResponseGarant
    
    class YandexRequest(ResponseGarant):
        def __init__(self):
            super().__init__()
            self.method = 'get'
            self.url = 'https://ya.ru/'
            
    def do_status_code(self):
        return self.response.text


    print(YandexRequest().get_rezult())
>ответ:
>
>`<body></body><script nonce='7cc08823771d91d242c073b32454fdb5'>var it = {"host":"https:\u002F\u002Fsso.ya.ru\u002Finstall?uuid=56435e04-2d88-496f-8e51-38b7785abd66","retpath":"https:\u002F\u002Fya.ru\u002F?nr=1"};(function() { var form = document.createElement('form'); var element1 = document.createElement('input'); var element2 = document.createElement('input'); element1.name = 'retpath'; element1.type = 'hidden'; element1.value = it.retpath; form.appendChild(element1); element2.name = 'container'; element2.type = 'hidden'; element2.value = '1659585699.10129169.wTwMc2KBuC2x0bJb.LuKtr2o6FfqR6MMY112sqaYyclyTBG7lyNeBwG0PtCPHQKP-yY9TyR52KO_ROPA7h8mT1adUcYZjj1kyfVhoBPWioDdXxZlwbKu0_m4W4rMcuFnWjLN10oxLxPcMBLvOMKqjFEQA428jce6qvo37XSl_aHWfNArPsg6NmOTmCYhzAcJwQqjTYoYePgjK3ndahWUJ9PJEyRkp9vuQTOTVU3Thi2E4YVha2Zn08KCGKm8xuvW-4fm72F6HixVMP3QspAkPrKCS993uHPIvmSzmQXhlp_JM1VFBZJcuE3HIL3hd0wZNcSSVdj9JWPN1WebRNsC8Tt0EBlQNY9SiR8QFMEJ2DbkNFPAwpDITd5DdqKTEOzozYXwLvNBv0WUpezpeYtM4rDmUJE7bKCgAzUg909XUXHBB3eajfAwUgZ_R1fMC2bRrEJdmUwhuH55CB8ED3f464zVvwDN3_OPCfUWaJZt4ftLRxZ-fFvN99LpDwcCbghRBF75NHhKnW0CQlO3x5d3rcHWomLpgoEGoTnDBQfaOlZpvGLpHZTV3ygINNa9xfB7eotdLPPFUCHFXV4nOiT8.FauV-8lZR80cM5b4Yg-Dmw'; form.appendChild(element2); form.method = 'POST'; form.action = it.host; document.body.appendChild(form); form.submit();})();</script>`

в примере выше мы обратились к обьекту self.response это экземпляр обьекта requests.models.Response и взяли у него атрибут texт, таким образом мы можем обращатся
к методам и атрибутам response экземпляра requests.models.Response.
Так же мы можем явно обозначить атрибутом self.success успешность запроса, поставив его в то место которое сигнализирует об успешном запросе

    from garant_success_requests.custom_requests import ResponseGarant

        class YandexRequest(ResponseGarant):
            def __init__(self):
                super().__init__()
                self.method = 'get'
                self.url = 'https://ya.ru/'

            def do_status_code(self):
                self.success = True
                return self.response.text

        yr = YandexRequest()
        yr.get_rezult()

        if yr.success is True:            
            print('Выполним условия в случае успеха')
        else:
            print('Выполним условия в случае неудачи')
     





    


