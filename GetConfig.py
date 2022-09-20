import configparser
import os
import sys
# import log_print as log

path = sys.argv[0]
pathl = path.split('\\')
local = path.replace(pathl[len(pathl) - 1], 'config.ini')
if not os.path.exists(local):
    raise Exception('config.ini is not exist!')
config = configparser.ConfigParser()
config.read(local, encoding='utf-8')


def getConfigDict(section):
    config_dict = dict(config.items(section))
    for key, value in config_dict.items():
        config_dict[key] = eval(value)
    return config_dict


class ConfigInfo(object):
    def __init__(self):
        self.ComboBox = getConfigDict('ComboBox')
        self.exe = getConfigDict('EXE')
        self.product = getConfigDict("Product")



if __name__ == "__main__":
    config = ConfigInfo()
    print(config.ComboBox)
    print(config.exe)
    print(config.product)
# # 获取全部的section
# def readConfig():
#     secs = config.sections()
#     print('全部section：' + str(secs))
#     return secs

# options = config.options("Mysql-Database")  # 获取某个section名为Mysql-Database所对应的键
# print(options)
#
# items = config.items("Mysql-Database")  # 获取section名为Mysql-Database所对应的全部键值对
# print(items)
#
# host = config.get("FTP-LINK", "host")  # 获取[Mysql-Database]中host对应的值
# print(host)


# # 获取具体的键对应的值
# def getConfig(section, option):
#     return config.get(section, option)
