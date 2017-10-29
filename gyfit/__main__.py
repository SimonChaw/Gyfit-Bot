# -*- coding: utf-8 -*-
import praw
import time
import logging
import helpers

#handler = logging.StreamHandler()
#handler.setLevel(logging.DEBUG)
#logger = logging.getLogger('prawcore')
#logger.setLevel(logging.DEBUG)
#logger.addHandler(handler)

r = praw.Reddit('bot1', user_agent='bot1 user agent')



subreddit = r.subreddit('WinStupidPrizes')
for submission in subreddit.stream.submissions():#get new submissions in this subreddit
    if "youtube" in submission.url:# if the url is a youtube link
        submission.comments.replace_more(limit=0)#Get all comments in post
        comments = submission.comments.list()
        for comment in comments:#Check if a user is requesting the help of Gyfit-Bot
            if comment.body == '!Gyfit':
                print 'Got one!' ##we found someone who wants the bots help!
                print comment.author
                if helpers.getVideoLength(submission.url.split('=')[1]):
                    #its the proper length
                    comment.reply("Help is on the way!")
