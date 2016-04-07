from bs4 import BeautifulSoup as bs
import re

def cleanhtml(raw_html):
	cleanr =re.compile('<.*?>')
	jcleanr =re.compile('\$.*;')
	spaces =re.compile('\s+')
	cleantext = re.sub(cleanr,'', raw_html)
	cleantext = re.sub(jcleanr,'', cleantext)
	cleantext = re.sub(spaces,' ', cleantext)
	return cleantext
def grabNews(url,html):
	try:
		soup = bs(html)
		dic={}
		details = soup.select("ul.dArticle")[0]
		dic["source"] = details.select("li")[0].getText()
		dic["time"] = details.select("li")[2].getText()
		#print soup.select("html")
		div = soup.select("#fontSize-2")[0]
		dic["body"] = cleanhtml(str(div))
		print dic["body"]
		dic["title"] = soup.select('meta[itemprop="name"]')[0].get("content")
		dic["image"] = soup.select('meta[itemprop="image"]')[0].get("content")
		dic["meta_description"] = soup.select('meta[itemprop="description"]')[0].get("content")
		dic["_id"] = url.replace(".","#d#")
		return dic
	except:
		return None

def fetchLinks(html):
	soup = bs(html)
	aas = soup.find_all("a")
	links=[]
	for a in aas:
		if " /news/" in " "+a.get("href"):
			links.append("http://www.bhaskar.com"+a.get("href"))

	return links
