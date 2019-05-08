import requests
import re

def getHtmlText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePage(ulist,html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ulist.append([price, title])
	except:
		print('')

def printResult(ulist):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format('序号', '价格', '商品名称'))
	count = 0
	for g in ulist:
		count = count + 1
		print(tplt.format(count, g[0], g[1]))

if __name__ == "__main__":
	goods = "水杯"
	start_url = 'https://s.taobao.com/search?q=' + goods
	depth = 2
	flist = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44 * i)
			html = getHtmlText(url)
			parsePage(flist, html)
		except:
			print("error")
	printResult(flist)








