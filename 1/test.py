import time
#----------------------------------------------------------------------
def lianjie(a,b):
    """"""
    c = a + b
    
    return c

#----------------------------------------------------------------------
def url_list(url_file):
    """"""
    a = 1
    with open(url_file) as u:
        url_list = u.readlines()
        for i in url_list:
            print 'NO.' + str(a) + ':' + i
            a = a + 1
        #return url_list
#----------------------------------------------------------------------
def path_list(path_file):
    """"""
    with open(path_file) as p:
        b = 1
        path = p.readlines()
        for i in path:
            print '[+] NO.' + str(b) + ":" + i
            b = b + 1
            time.sleep(1)
        
    
path_list('shell.txt')

    
    