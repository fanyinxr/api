
import os
import time
import unittest
import HTMLTestRunner

#执行所有用例并发送报告
# '''
# 第一步加载用例
# 第二部执行用例
#
# '''

cur_path=os.path.dirname(os.path.realpath(__file__))

def add_case(caseName="case",rule="test*.py"):
    #加载所有用例
    case_path=os.path.join(cur_path,caseName)

    #如果不存在case文件夹，自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    print("test case path:%s"%case_path)
    #定义discover方法的参数
    discover=unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)

    print(discover)
    return discover

def run_case(all_case,reportName="report"):
    #执行所有用例
    # now=time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path=os.path.join(cur_path,reportName)

    #如果不存在report文件夹，自动创建一个
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath=os.path.join(report_path,"result.html")
    print("report path:%s"%report_path)
    fp=open(report_abspath,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"自动化测试报告，测试结果如下：",description=u"用例执行情况：")

    runner.run(all_case)
    fp.close()

if __name__=="__main__":

    #加载用例
    all_case=add_case()

    #生成测试报告路径
    run_case(all_case)
