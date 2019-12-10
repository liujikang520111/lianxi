import requests
import api

class ApiEmployee:
    #初始化
    def __init__(self):
        self.url = api.BASE_URL + "/api/sys/user"
        self.url_employee = api.BASE_URL + "/api/sys/user/{}"

    #添加员工
    def api_post(self,username,mobile,workNumber):
        data = {"username":username,
                "mobile":mobile,
                "workNumber":workNumber}
        #调用post方法
        return requests.post(url=self.url,json=data,headers=api.headers)
    #查询员工
    def api_get(self):
        return requests.get(url=self.url_employee.format(api.user_id),headers=api.headers)
    #更新员工
    def api_put(self,username):
        data = {"username":username}
        return requests.put(url=self.url_employee.format(api.user_id),json=data,headers=api.headers)
    #删除员工
    def api_delete(self,user_id):
        return requests.delete(self.url_employee.format(user_id),headers=api.headers)
        pass