
import datetime
from info_url import Url_Check
from Config import FileConfig
from multiprocessing.dummy import Pool
from url_list import get_url_list



t1 = datetime.datetime.now()
pool = Pool(processes=10)


#----------------------------------------------------------------------
def start(i):
    """"""
    
    data_url = Url_Check(i)
    data_url.update_mongo()
    url_list = get_url_list(FileConfig.URLFILE)
    print url_list.index(i)
try:
    pool.map(start,(get_url_list(FileConfig.URLFILE)))
    print 'Starting',multiprocessing.current_process().name
    print 'success'
except Exception,e:
    pass


    

pool.close()
pool.join()

print 'Multiprocess Scanning Completed in  ', datetime.datetime.now() - t1