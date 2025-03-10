from locust import HttpUser, between

from generic.request_client import RequestClient


class Base(HttpUser):
    abstract = True
    host = 'https://qa.projectqa.zingworks.com'
    wait_time = between(0.1, 1)

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)
        self._request = RequestClient(client=self.client)

    def on_start(self):
        super(Base, self).on_start()

    def on_start(self):
        super(Base, self).on_start()
