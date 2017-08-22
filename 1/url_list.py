import header
import urllib2
import datetime
import requests
import random
from Config import FileConfig
from multiprocessing.dummy import Pool

#----------------------------------------------------------------------
def qc(info):
    
    return info.strip('\r').strip('\n') 

#----------------------------------------------------------------------
def link_code(url):
    """"""
    page_content = ''
    try:       
        request = urllib2.Request(url,headers=header.get_header())  
        html_url = requests.get(url, timeout=random.randint(3,8))
        
        #print type(html_url.status_code)
        url_code = html_url.status_code
        #response = urllib2.urlopen(request)  
        #print html_url.status_code
        if url_code == 200:
            return True
        else:
            pass    
        
    except Exception,e:
        pass
    
  
#link_code('https://www.xiaoz.me/')
a = []
#----------------------------------------------------------------------
def get_url_list(url_file):
    """"""
    with open(url_file) as urls:
        url = urls.readlines()
        url_list = list(set(map(qc,url)))
        try:
            for i in url_list:
                if link_code(i):
                    a.append(i)
        except Exception,e:
            pass
        return a
#get_url_list(FileConfig.URLFILE)