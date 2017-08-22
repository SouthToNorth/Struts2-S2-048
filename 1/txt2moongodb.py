import pymongo
import mongo
import Config
from url_list import qc

with open(Config.FileConfig.SHELLFILE) as s:
    shell = s.readlines()
    shell_list = map(qc, shell)
    mongo.ls_WSPath.save({'Webshell Path':shell_list})
    print '1'
    
    