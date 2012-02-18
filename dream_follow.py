#!/usr/bin/env python

# imports
from sys import exit
import tweepy
import settings

# import exceptions
from urllib2 import HTTPError
from random import choice

# globals
magic_words = ['dream', 'lucid', 'dreaming', 'had a dream', 'hack', 'lucidity', 'yoga', 'organic', 'new age', 'lsd', 'weed', 'dxm']

def debug_print(text):
    """Print text if debugging mode is on"""
    if settings.debug:
        print text

def main():
    auth = tweepy.OAuthHandler(consumer_key=settings.consumer_key,
        consumer_secret=settings.consumer_secret)
    auth.set_access_token(settings.access_key, settings.access_secret)

    api = tweepy.API(auth_handler=auth, secure=True, retry_count=3)

    word = choice(magic_words)
    debug_print('Searching for ' + word)
    search = api.search(word)
    for s in search:
        if not api.exists_friendship(s.from_user, settings.username):
            debug_print(str(s.from_user) + " doesn't follow you! Following!")
            api.create_friendship(s.from_user)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()