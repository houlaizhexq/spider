#coding:utf-8
#获取动态网页中的所有url
from selenium import webdriver
from bs4 import BeautifulSoup
from re import search
from tld import get_tld

print "开始爬行..."

url = 'http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000'

#获取当前地址的域名，便于限制爬行范围为当前网站
try:
    host = get_tld(url)
except Exception as e:
    print "unkonw"

print "当前域名为：" + str(host.encode("utf-8"))
driver = webdriver.PhantomJS()

driver.get(url)

soup = BeautifulSoup(driver.page_source,"lxml")

linkes = soup.find_all('a')

for l in linkes:
    match = search('href="([^(javascript)][^#][\S]+)"',str(l))
    if match:
        temp = str(match.group(1))
        if temp.startswith("http"):
            if get_tld(temp) == host:
                print temp
        else:
            temp = "http://www.liaoxuefeng.com" + temp
            print temp