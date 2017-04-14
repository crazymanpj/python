import ConfigParser

def writeinivalue(configfile, section, key, value):
	config = ConfigParser.ConfigParser()
	config.read(configfile)
	if not config.has_section(section):
		temp = config.add_section(section)
	config.set(section, key, value)
	config.write(open(configfile, "r+"))


writeinivalue("mailconfig.ini", "searchmail", "start","66")