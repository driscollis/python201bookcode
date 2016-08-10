import praw

red = praw.Reddit(user_agent='pyred')
print(red.get_top())

for i in red.get_top():
     print(i)