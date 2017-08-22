
import urllib2
#----------------------------------------------------------------------
def waf_url(url):
    """"""
    
resp = urllib2.urlopen('http://www.shiep.edu.cn')

print resp.headers
print resp.headers['Server']

if resp.headers["ETag"]:
    print '111'
else:
    print 222
    pass
