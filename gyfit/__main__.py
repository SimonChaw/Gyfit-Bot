import praw
import time
import logging

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('prawcore')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

r = praw.Reddit('bot1', user_agent='bot1 user agent')

polite_users = set()   # to avoid duplicates
# assume you have a Reddit instance bound to variable `reddit`
subreddit = r.subreddit('redditdev')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
print(subreddit.description)   # Output: A subreddit for discussion of ...
