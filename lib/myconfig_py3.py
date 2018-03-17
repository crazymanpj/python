# encoding: UTF-8
# env: python3
# Date:    2017-01-12
# Author:  pangjian
# version: 1.1
import configparser


def getconfigvalue(filepath, setionname, key):
    try:
        configfile = open(filepath, "r")
        parser = configparser.ConfigParser()
        config = parser
        config.read_file(configfile)
        configfile.close()
        value = config.get(setionname, key)
        return value
    except:
        return False


def writeinivalue(configfile, section, key, value):
    config = configparser.ConfigParser()
    config.read(configfile)
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, key, value)
    config.write(open(configfile, "r+"))

if __name__=='__main__':
    t = getconfigvalue('d:\kuaipan\python\Django\dbmakepack\lib\stconfig.txt', 'singletonthread', 'isworking')
    writeinivalue('d:\kuaipan\python\Django\dbmakepack\lib\stconfig.txt', 'singletonthread', 'isworking', '0')
