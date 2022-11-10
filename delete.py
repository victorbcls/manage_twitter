import tweepy
from time import sleep

api_key = ""
api_key_secret = ""
bearer = ""
client_id = ""
client_secret = ""
access_token = ""
access_token_secret = ""


client = tweepy.Client(
    bearer_token=bearer,
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)
first_tweet_id = ""  # get tweets older than this one
user_id = ""  # your user id
while True:
    response = client.get_users_tweets(
        max_results=50,
        id=user_id,
        tweet_fields=["created_at"],
        until_id=first_tweet_id,
    )
    for tweet in response.data:
        try:
            client.delete_tweet(tweet.id, user_auth=True)
            print(f'Deleted: "{tweet}"')
        except Exception as e:
            # twitter 2.0 api only allows 50 delete requests per 15min
            print("SLEEPING 15 MIN")
            sleep(15 * 60)
