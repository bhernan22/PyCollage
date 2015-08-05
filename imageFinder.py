import urllib2
import simplejson
from StringIO import StringIO
from PIL import Image
import requests
import time
import os
import json
from requests.exceptions import ConnectionError

def ImageSearch(query, path):

    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + query + '&start=%d'

    BASE_PATH = os.path.join(path, query)

    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    start = 0
    while( start < 60):
        r = requests.get(BASE_URL % start)    
        for image_info in json.loads(r.text)['responseData']['results']:
            url = image_info['unescapedUrl']
            try:
                image_r = requests.get(url)
            except ConnectionError, e:
                print 'Failed to download %s' % url
                continue
            title = image_info['titleNoFormatting'].replace('/','').replace('\\','')
    
            file = open(os.path.join(BASE_PATH, '%s.jpg') % title, 'w')
            try:
                Image.open(StringIO(r.content)).save(file, 'JPEG')
            except IOError, e:
                print 'Failed to save %s' % url
                continue
            finally:
                file.close()
    print start
    start += 3
    time.sleep(1.5)
        


ImageSearch('Fairies', 'temps')
