###--- IMPORTS ---###
import subprocess
import urllib.request


###--- check if connected ---###
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


print('yes' if connect() else 'no')
