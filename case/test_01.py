import unittest
import requests
from common.logger import Log


class Blog_login(unittest.TestCase):
    log = Log()
    def login(self, username, psw, reme=True):
        url = "https://passport.womai.com/login/login.do"

        headers = {"Accept": "application/json, text/javascript, */*",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Accept-Language": "zh-CN,zh;q=0.9",
                   "Connection": "keep-alive",
                   "Content-Length": "163",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Host": "passport.womai.com",
                   # "Referer": "https://passport.womai.com/redirect/redirect.do?mid=0&returnUrl=http%3A%2F%2Fwww.womai.com%2Findex-31000-0.htm",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
                   "X-Requested-With": "XMLHttpRequest"

                   }
        json_data = {"input1": username,
                "input2": psw,
                "remember": reme}


        res = requests.post(url, headers=headers, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        self.log.info("我买网登陆结果：%s"%result1)
        return res.json()      # 返回json

    def test_login1(self):
        u'''测试登录：正确账号，正确密码'''
        self.log.info("------登录成功用例：start!---------")
        username = "lklkerry",
        self.log.info("输入正确账号：%s"%username)
        psw = "lkl19971114",
        self.log.info("输入正确密码：%s"%psw )
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual('2',result["msg"])
        self.log.info("------pass!---------")

    def test_login2(self):
        u'''测试登录：正确账号，错误密码'''
        self.log.info("------登录失败用例：start!---------")
        username = "lklkerry",
        self.log.info("输入正确账号：%s"%username)
        psw = "lkl199711",
        self.log.info("输入错误密码：%s"%psw)
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual('2',result["msg"])
        self.log.info("------pass!---------")


if __name__ == "__main__":
    unittest.main()
