from configparser import ConfigParser

class ReadConfig:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('./config.ini')

    def get_server(self,name):
        print(self.config.sections())

        #读取配置文件
        value = self.config.get("testServer",name)
        return value