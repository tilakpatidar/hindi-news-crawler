import os
from multiprocessing import Pool
import config

def runCrawler(crawler_name):
	"""
		Takes a crawler name from list of crawlers in ./crawlers dir
		Executes main function of the import crawler_name
	"""
	try:
		print "from crawlers import %s"%(crawler_name)
		exec("from crawlers import %s"%(crawler_name))
		print crawler_name+".main()"
		exec(crawler_name+".main()")
	except Exception, e:
		print e
		pass





#fetch list of available crawlers
crawlers = os.listdir("./crawlers")

pool = Pool(config.getConfig("concurrent_crawlers"))

pool.map(runCrawler, crawlers)



