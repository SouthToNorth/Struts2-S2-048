import mongo
import pymongo
from Config import FileConfig
import sys
from url_list import qc
from url_list import link_code

reload(sys)
sys.setdefaultencoding('utf8')

#----------------------------------------------------------------------
def judge_webshell(url):
    """"""
    conn = mongo.ls_WSPath
    webshell_data = conn.find()
    for i in webshell_data:
        for webshell_path in i['Webshell Path']:
            print url + webshell_path
            status_code = link_code(url+webshell_path)
judge_webshell('www.baidu.com')
    
    
    