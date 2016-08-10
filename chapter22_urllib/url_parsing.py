from urllib.parse import urlparse

result = urlparse('https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa')
print(result)
print(result.netloc)
print(result.geturl())