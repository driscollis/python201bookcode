import urllib.request

user_agent = ' Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
url = 'http://www.whatsmyua.com/'
headers = {'User-Agent': user_agent}
request = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(request) as response:
    with open('/home/mike/Desktop/user_agent.html', 'wb') as out:
        out.write(response.read())