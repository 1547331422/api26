from test.case.basecase import BaseCase
from lib.db1 import *
import json

class test_user_reg(BaseCase):
    def test_user_reg_ok(self):
        case_data=self.get_case_data("reg_ok")
        username=json.loads(case_data["args"])["userName"]

        if check_user(username):
            del_user(username)
            self.send_request(case_data)

            self.assertTrue(check_user(username))
            del_user(username)
    def test_user_reg_fail(self):
        case_data=self.get_case_data("reg_err")
        name=json.loads(case_data["args"])["userName"]

        if not check_user(name):
            add_user(name,"123456")
            self.send_request(case_data)

            self.assertTrue(check_user(name))