import logging
import time
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Log():
    def __init__(self):
        #文件命名
        self.logname=os.path.join(log_path,"%s.log"%time.strftime('%Y_%m_%d'))
        self.loggeer=logging.getLogger()
        self.loggeer.setLevel(logging.DEBUG)

        #日志输出格式
        self.formatter=logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')


    def __console(self,level,message):
        fh=logging.FileHandler(self.logname,'a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.loggeer.addHandler(fh)

        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.loggeer.addHandler(ch)

        if level =='info':
            self.loggeer.info(message)
        elif level =='debug':
            self.loggeer.debug(message)
        elif level =='warning':
            self.loggeer.warning(message)
        elif level =='error':
            self.loggeer.error(message)

        #避免日志输出重复
        self.loggeer.removeHandler(ch)
        self.loggeer.removeHandler(fh)

        #关闭打开的文件
        fh.close()

    def debug(self,message):
        self.__console('debug',message)

    def info(self,message):
        self.__console('info',message)

    def warning(self,message):
        self.__console('warning',message)

    def error(self,message):
        self.__console('error',message)


if __name__ == "__main":
    log = Log()
    log.info("---测试开始---")
    log.info("操作步骤1,2,3")
    log.warning("---测试结束---")


