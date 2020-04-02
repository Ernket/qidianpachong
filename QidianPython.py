# -*-coding:utf-8-*-
# -*-Auther:Elapse-*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
def get_url(url):
	html=urlopen("https:"+url)
	bsObj=BeautifulSoup(html,"html5lib")
	neir=bsObj.select('#readBtn')
	nurl=neir[0].get('href')
	return nurl

def downloadtxt(bkurl,bkname):
	url="https:"+get_url(bkurl)
	while True:
		try:
			html=urlopen(url)
			bsObj=BeautifulSoup(html,"html5lib")
			bt=bsObj.find('title') #查找小说名字
			chapter=bsObj.find("div",{"class","read-content"}) #查找小说
			chapter=chapter.find_all("p")
			fo=open(bkname+".txt","a",encoding='UTF-8') #保存txt文件，并将名字设置为小说名
			fo.write("\n"+bt.get_text()+"\n") #内容写入
			for i in chapter:
				fo.write("\n"+i.get_text().replace(" ","")) #内容写入
			fo.close() #关闭文件
			bsoup=bsObj.find("",{"id":"j_chapterNext"}) #获取下一章的url
			url="http:"+bsoup.get('href')+".html" #拼接语句
		except:
			print ("抓取完毕.....")
			time.sleep(2)
			break
			
print('''

 /$$$$$$$$ /$$
| $$_____/| $$
| $$      | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$
| $$$$$   | $$ |____  $$ /$$__  $$ /$$_____/ /$$__  $$
| $$__/   | $$  /$$$$$$$| $$  \ $$|  $$$$$$ | $$$$$$$$
| $$      | $$ /$$__  $$| $$  | $$ \____  $$| $$_____/
| $$$$$$$$| $$|  $$$$$$$| $$$$$$$/ /$$$$$$$/|  $$$$$$$
|________/|__/ \_______/| $$____/ |_______/  \_______/
                        | $$
                        | $$
                        |__/

''')
url="https://www.qidian.com/free"
html=urlopen(url)
bsObj=BeautifulSoup(html,"html5lib")
fname=bsObj.select('div > h4 > a')
book_name=[]
book_url=[]
num=1
for i in fname:
	if num==7:
		break
	a=i.get_text()
	print("["+str(num)+"]: "+a)
	b=i.get('href')
	book_name.append(a)
	book_url.append(b)
	num+=1
try:
	whichbook=int(input("请选择书籍ID："))
except:
	print("ID错误，程序即将退出...")
	time.sleep(3)
bkurl=book_url[whichbook-1]
bkname=book_name[whichbook-1]
downloadtxt(bkurl,bkname)
