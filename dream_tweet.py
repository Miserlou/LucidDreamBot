#!/usr/bin/env python

# imports
from sys import exit
import tweepy
import settings

# import exceptions
from urllib2 import HTTPError
from random import choice
import random

# globals
tweets = ['Reality check: Are you dreaming right now?',
            'Is this a dream?',
            'Are you dreaming? Stand up and try to turn the lights on. Did they change?',
            'Dreamcheck! Are you dreaming right now? Please RT!',
            'Is this the real life? Is it just fantasy?',
            'Whats your dream state? Are you asleep right now? Please RT!',
            'Dreamcheck! Look at a digital clock! Are you dreaming?',
            'Get better at dreaming by being mindful of your dreams. Are you asleep?',
            'Are you dreaming right now? #lucid #dream #check',
            'Are you dreaming right now?',
            'Lucid dreaming is better than sex.',
            'Are you asleep right now? This could be a dream.',
            'Do you know how to lucid dream? Follow for reality reminders!',
            'Lucid dream reminder! Are you dreaming right now?',
            'Are you dreaming right now? Try to fly around!',
            'Question reality! Are you dreaming right now?',
            'Next time you wake up from your nap, think about your dreams and go back to sleep!',
            '#lucid #dream #reality #check',
            'Sanity is a madness put to good uses; waking life is a dream controlled.',
            'Are you dreaming right now? See if you can conjure objects!']

def debug_print(text):
    """Print text if debugging mode is on"""
    if settings.debug:
        print text

def main():

    # Cron jitter
    rand = random.randint(0, 60)
    rand = random.randint(0, 60)

    if rand > 4:
        debug_print(rand)
        debug_print("Not tweeting.")
        exit()

    auth = tweepy.OAuthHandler(consumer_key=settings.consumer_key,
        consumer_secret=settings.consumer_secret)
    auth.set_access_token(settings.access_key, settings.access_secret)

    api = tweepy.API(auth_handler=auth, secure=True, retry_count=3)

    tweet = choice(tweets)
    debug_print("Tweeting!")
    debug_print(tweet)
    api.update_status(tweet)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()