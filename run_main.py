import unittest
import time
import os
import HTMLTestRunner

#执行所有用例并发送报告
'''
第一步加载用例
第二部执行用例

'''

#当前版本文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName="case",rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path,caseName)
    #如果不存在case这个文件夹，就自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)

    print("test case path:%s"%case_path)
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case,reportName="report"):
    '''第二步：执行所有的用例，并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    print("report path :%s"%report_abspath)
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告，测试结果如下：',
                                           description=u'用例执行情况：')

    #调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ =="__main__":
    #加载用例
    all_case = add_case()

    #执行用例
    run_case(all_case)
