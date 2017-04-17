import re
import urllib2

from bs4 import BeautifulSoup


def getlist(baseurl="https://www.torrentso.com/cn/s/n0",x=400,y=500):
    zz=range(x,y)
    zz=[baseurl+str(i)+"/" for i in zz]
    return zz

def checkG(s):
    if len(re.findall("GB",str(s)))>0 and len(re.findall("Tokyo",str(s)))>0:
        return True
    else:
        return False


def getmagnet(url):
    ss=urllib2.urlopen(url)
    page=ss.readlines()
    return re.findall('''(magnet:?[^\"]+)</t''',str(page))


def getpage(url):
    f=urllib2.urlopen(url)
    soup=BeautifulSoup(f)
    return soup


def getM(m,n):
    all_list = getlist(x=m, y=n)
    z = map(getpage, all_list)
    href = []
    for i in z:
        try:
            #print filter(checkG, i.find_all("li"))[0]("a")[0]["href"]
            href.append(filter(checkG, i.find_all("li"))[0]("a")[0]["href"])
        except:
            print ">>>>>>>>>>>"
    hh = map(getmagnet, href)
    for i in hh:
        print i[0]


getM(300,349)
