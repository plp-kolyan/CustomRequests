from requestsgarant import RequestsGarant

class WappiPro(RequestsGarant):
    def __init__(self, profile_id, api_key):
        super().__init__()
        self.profile_id = profile_id
        self.headers = {
            'Authorization': api_key
        }


class WappiProSendMess(WappiPro):
    def __init__(self, profile_id, api_key, mess, phone):
        super().__init__(profile_id, api_key)

        self.url = f'https://wappi.pro/api/sync/message/send?profile_id={profile_id}'
        self.json = {
                "body": mess,
                "recipient": phone
            }

        self.method = 'post'

    def do_json(self):
        status = self.response_json.get('status')
        if status is not None:
            if status == 'done':
                self.success = True
                return status

class WappiProMessAllGet(WappiPro):
    def __init__(self, profile_id, api_key, limit, offset, date, order):
        super().__init__(profile_id, api_key)

        self.url = f'https://wappi.pro/api/sync/messages/all/get'
        self.params = {
            "profile_id": self.profile_id,
            "limit": limit,
            "offset": offset,
            "date": date,
            "order": order
        }
        self.headers = {
            'Authorization': api_key
        }
        self.method = 'get'

    def do_json(self):
        messages = self.response_json.get('messages')
        if messages is not None:
            self.success = True
            return messages