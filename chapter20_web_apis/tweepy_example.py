import tweepy

# Update the following four pieces of data with your own
key = 'random_key'
secret = 'random_secret'
access_token = 'access_token'
access_secret = 'super_secret'

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

my_tweets = api.user_timeline()
for tweet in my_tweets:
    print(tweet.text)

# Get top 5 Python articles on Reddit
python = red.get_subreddit('python')
submissions = python.get_hot(limit=5)
for submission in submissions:
    print(submission)

# Get comments on a specific article
id = '4q2lxb'
submission = red.get_submission(submission_id=id)
comments = submission.comments
print(comments[0].author)
print(comments[0].body)