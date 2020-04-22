# encoding: UTF-8
import ConfigParser

def getconfigvalue(filepath, setionname, key):
    try:
        configfile = open(filepath, "r")
        config = ConfigParser.ConfigParser()
        config.readfp(configfile)
        configfile.close()
        value = config.get(setionname, key)
        return value
    except:
        return False 

def writeinivalue(configfile, section, key, value):
	config = ConfigParser.ConfigParser()
	config.read(configfile)
	if not config.has_section(section):
		temp = config.add_section(section)
	config.set(section, key, value)
	config.write(open(configfile, "r+"))
