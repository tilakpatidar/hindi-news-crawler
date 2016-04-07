import urllib2 as u
import time
import parser
import threading

from pymongo import MongoClient as mc

db = mc()
db = db["news"]
col = db["bhaskar"]


START_DATE = time.strptime(open("./crawlers/bhaskar/start_date.txt","r").read(), "%Y-%m-%d")
START_DATE = time.mktime(START_DATE)
BASE_URL = "http://www.bhaskar.com/archives/"

def main():
	dates = []
	#generate dates to be crawled
	days = ( int(time.time()) - int(START_DATE) ) / (3600*24)
	PREV_DATE = START_DATE
	for i in range(days):
		day = int(PREV_DATE) + (3600*24)
		PREV_DATE = day
		day =  time.strftime("%Y-%m-%d", time.localtime(int(day))) 
		dates.append(day)

	#fetch for each date and insert
	for day in dates:
		print BASE_URL+day+"/"
		fetch_url = BASE_URL+day+"/"
		try:
			html = u.urlopen(fetch_url).read()
			p = parser.fetchLinks(html)
			for url in p:
				fi = col.find_one({"_id":url.replace(".","#")})
				if fi is None:
					f = fetchNews(url)
					if f is not None:
						col.insert_one(f)
			col.insert_one({"_id":fetch_url.replace(".","#")})
		except:
			pass



def fetchNews(url):
	print url
	try:
		html = u.urlopen(url).read()
		dic = parser.grabNews(url,html)
		return dic
	except Exception, e:
		return None
