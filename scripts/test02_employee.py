import unittest
import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = ApiEmployee()
    def test01_post(self,username="zhaoxv",mobile="13822232222",wordNumber="831043"):
        r = self.api.api_post(username,mobile,wordNumber)
        print("新增员工为:", r.json())
        api.user_id = r.json().get("data").get("id")
        print("新增员工ID为:",api.user_id)
        assert_common(self, r)
    def test02_get(self):
        r = self.api.api_get()
        print("查询的结果为：",r.json())
        assert_common(self,r)

    def test03_put(self,username="zhaoxvedi"):
        r = self.api.api_put(username)
        print(r.json())

    def test04_delete(self):
        r = self.api.api_delete(user_id=api.user_id)
        print("删除后的数据为:",r.json())
        assert_common(self,r)
        pass
