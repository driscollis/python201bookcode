import urllib.request
import urllib.parse


data = urllib.parse.urlencode({'q': 'Python'})
url = 'http://duckduckgo.com/html/'
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)
with open('/home/mike/Desktop/results.html', 'wb') as f:
    f.write(response.read())