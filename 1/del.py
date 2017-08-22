import tld
import requests
import urllib2
import random


def link_code(url):
    """"""
    try:       
        #request = urllib2.Request(url,headers=header.get_header())  
        html_url = requests.get(url, timeout=random.randint(3,8))

        url_code = html_url.status_code

        if url_code == 200:
            print url_code  
            return url
        else:
            pass    

    except Exception,e:
        print 'xxx'
        pass        

#link_code('http://www.baidu.com')

#----------------------------------------------------------------------
def input_url(url_file):
    """""" 
    w1 = open('target_200_url.txt','w+')
    with open(url_file) as f:
        urls = f.readlines()
        for i in urls:
            i = i.strip('\n').strip('\r')
            print i
            try:
                url_200 = link_code(i)
                
                w1.writelines(i)
                w1.write('\n')
                print i + '    yes!'
            except Exception,e:
                print i  + str(e)
               
#input_url('formal_url.txt')


a = [] 
#----------------------------------------------------------------------
def ceshi_url(url_file):
    """"""
    with open(url_file) as w:
        urls = w.readlines()
        for i in urls:
            i = i.strip('\n').strip('\r')
            try:
                url = tld.get_tld(i)
                list_url = 'http://' + url
                a.append(list_url)
                
            except Exception,e:
                print str(e)
    
#ceshi_url('formal_url.txt')
#g = open('url.txt','w+')
#a = list(set(a))
#print len(a)
#for i in a:
    #print i
    #g.writelines(i)
    #g.writelines('\n')
    import unittest
    
from selenium import webdriver
from xvfbwrapper import Xvfb
    
    
class TestPages(unittest.TestCase):

    def setUp(self):
        self.xvfb = Xvfb(width=1280, height=720)
        self.addCleanup(self.xvfb.stop)
        self.xvfb.start()
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testUbuntuHomepage(self):
        self.browser.get('http://www.ubuntu.com')
        self.assertIn('Ubuntu', self.browser.title)

    
    
if __name__ == '__main__':
    unittest.main()