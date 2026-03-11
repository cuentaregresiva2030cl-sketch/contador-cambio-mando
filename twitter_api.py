import tweepy
import os

def post_tweet_api(text, image):

    auth = tweepy.OAuth1UserHandler(
        os.environ["API_KEY"],
        os.environ["API_SECRET"],
        os.environ["ACCESS_TOKEN"],
        os.environ["ACCESS_TOKEN_SECRET"]
    )

    api = tweepy.API(auth)

    api.update_status_with_media(filename=image, status=text)
