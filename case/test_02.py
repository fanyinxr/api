import unittest
import requests
from common.logger import Log
class Test_Kuaidi(unittest.TestCase):
    #测试快递查询接口
    log = Log()
    def setUp(self):
        self.headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0:WOW64: rv:44.0) Gecko/20100101 Firefox/44"
        }

    def chaxun_kuaidi(self,danhao,kd,kd_name):
        #三个参数：单号，快递名称，快递中文名
        self.url="http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html"%(danhao,kd)
        self.log.info(u"测试url地址：%s"%self.url)

        #第一步发请求
        r =requests.get(self.url,headers=self.headers,verify=False)
        result = r.json()
        self.log.info(u"获取请求结果：%s"%result)

        #第二部获取结果
        self.log.info(u"获取公司名称：%s"%result['company'])
        data=result["data"]
        self.log.info(u"获取data内容：%s"%result["data"])
        get_result = data[0]['context']  #获取已签收状态
        self.log.info(u"获取已签收状态：%s"%get_result)

        #断言:测试结果与期望结果对比

        self.assertEqual(kd_name,result["company"])
        self.assertIn(u"已签收",get_result)


    def test_yuantong(self):
        self.log.info("-----------start---------!")
        danhao = '816608751876'
        kd='yuantong'
        kd_name="圆通快递"
        self.log.info(u"测试单号：%s  快递名称：%s"%(danhao,kd_name))
        self.chaxun_kuaidi(danhao,kd,kd_name)
        self.log.info("------------pass!----------!")




if __name__ == "__main__":
    unittest.main()



