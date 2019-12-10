import requests
import api

class ApiLogin:
    def __init__(self):
        self.url = api.BASE_URL + "/api/sys/login"

    def api_login(self,mobile,password):
        data = {"mobile":mobile,"password":password}
        return requests.post(url=self.url,json=data,headers=api.headers)