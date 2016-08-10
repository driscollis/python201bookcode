import requests

from bs4 import BeautifulSoup

url = 'https://twitter.com/mousevspython'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
tweets = soup.findAll('li', 'js-stream-item')
for item in range(len(soup.find_all('p', 'TweetTextSize'))):
    tweet_text = tweets[item].get_text()
    print(tweet_text)
    dt = tweets[item].find('a', 'tweet-timestamp')
    print('This was tweeted on ' + dt)