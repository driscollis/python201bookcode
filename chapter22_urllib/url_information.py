import urllib.request

url = urllib.request.urlopen('https://www.google.com/')
print(url.geturl())
print(url.info())
header = url.info()
header_str = header.as_string()
print(header_str)