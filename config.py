def getConfig(key):
	c= {
		"concurrent_crawlers":10,
	}
	try:
		return c[key]
	except Exception, KeyError:
		return None
	