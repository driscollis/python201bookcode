import urllib.request
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
tmp_file, header = urllib.request.urlretrieve(url)
with open('/home/mike/Desktop/test.zip', 'wb') as fobj:
    with open(tmp_file, 'rb') as tmp:
        fobj.write(tmp.read())