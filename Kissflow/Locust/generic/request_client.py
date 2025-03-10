from locust.clients import HttpSession


class RequestClient:

    def __init__(self, *args, **kwargs):
        self.api_key = 'Ak0fe883bf-ab31-456d-a5aa-b802034609cb'
        self.account_id = 'AcUZr0RbpnS3R'
        self.__client: HttpSession = kwargs.get('client')
        self.__headers = {'x-api-key': self.api_key}

    def get(self, url, name=None):
        response = self.__client.get(url, name=name, headers=self.__headers)
        print('GET:: Request Name:', name or url)
        print('GET:: Response status code:', response.status_code)
        print('GET:: Response text:', response.text)

        return response

    def post(self, url, json, name=None):
        response = self.__client.post(url, json=json, name=name, headers=self.__headers)
        print('POST:: Request Name:', name or url)
        print('POST:: Response status code:', response.status_code)
        print('POST:: Response text:', response.text)

        return response
