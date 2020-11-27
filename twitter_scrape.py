import os
import tweepy as tw
import pandas as pd
from secrete.Secretes import twitter

# https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
# https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens

auth = tw.OAuthHandler(twitter.consumer_key, twitter.consumer_secret)
auth.set_access_token(twitter.access_token, twitter.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#wildfires"
date_since = "2018-11-16"

tweets = tw.Cursor(api.search,
                   q=search_words,
                   lang="en",
                   since=date_since).items(5)

print([tweet.text for tweet in tweets])
