import tweepy
import time 
from datetime import datetime

apic="FeV0mvJ4RoqzjQPgr7ildDqwB"
apisc="84pHuoBjRQP0TdvSgXFCrOhxYSaNIqd2w3APCBeKyesPzNlz0p"

acc= "1386536718187208712-UAiid7BvQRqzueJRrkERu7h6SUTFJq"
acsc="jxbI21odi8DkKKGvPHMuMguXEv6PqnHb69cbFA3vTxZd4"

auth = tweepy.OAuthHandler(apic,apisc)

auth.set_access_token(acc,acsc)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()

print(user.screen_name)

 
search="Verified (Bed OR Blood OR Oxygen OR Fabiflu OR Plasma OR ICU OR Tocilizumab OR Ventilator OR Emergency OR Plasma OR donor OR OR CONCENTRATOR OR needed OR available OR SOS OR #COVIDIndiaResources OR #CovidNDIAInfo OR CovidHelp) min_faves:3 min_retweets:5 -filter:replies"
nrtweets=500
count=587

for tweet in tweepy.Cursor(api.search,search).items(nrtweets):
    try:
        tweet.retweet()
        time.sleep(600)
        count=count+1
        print("tweet retweeted",count)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
