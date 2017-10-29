# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import youtube_dl
import json
import urllib
import os
import ffmpeg

with open(os.path.dirname(__file__) + '/../youtube_api_key') as f:
    api_key = f.read()

def getVideoLength(video_id):
    print video_id
    searchUrl="https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=contentDetails"
    response = urllib.urlopen(searchUrl).read()
    data = json.loads(response)
    all_data=data['items']
    contentDetails=all_data[0]['contentDetails']
    duration=contentDetails['duration']
    return isProperLength(duration)

def isProperLength(duration):
    #Duration will look like PT6M22S or PT1H20M29S or PT20S
    if 'H' not in duration:
        #check for M
        if 'M' not in duration:
            return True
        else:
            #Check if M is equal to 1 and S are 30 or below
            time=duration.split('PT')
            MS = "".join(time).split('M')
            M = int(MS[0])
            S = int(MS[1].split('S')[0])
            if M == 1 and S <= 30:
                return True
            else:
                return False
    else:
        return False

def downloadVideo(url):
    ydl_opts = {
        #'outtmpl': os.path.dirname(__file__) + '/../videos/%(title)s-%(id)s.%(ext)s'
        'outtmpl': os.path.dirname(__file__) + '/../videos/vid.mp4'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        toGif(os.path.dirname(__file__) + '/../videos/vid.mp4')


def toGif(vidPath):
    return True
