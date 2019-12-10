def assert_common(self,response,status_code=200,message="操作成功！"):
    #状态码
    self.assertEqual(status_code,response.status_code)
    #断言success
    self.assertTrue(response.json().get("success"))
    #code
    self.assertEqual(10000, response.json().get("code"))
    #断言msg
    self.assertEqual(message, response.json().get("message"))
