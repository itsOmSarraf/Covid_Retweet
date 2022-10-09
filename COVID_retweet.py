#this is a code made for a TWITTER BOT : "@COVID_retweet" by "@itsOMSARRAF_" 

#__main__

import tweepy
import time 

apic= ""# add api_code 
apisc="" # add api_secret_code

acc= ""#add account_code
acsc= ""# add acount_secret_code             



cnt=open(r"C:\\Users\\Dell\\Desktop\\bot.txt","r+")

counts=cnt.read()

count=int(counts)

auth = tweepy.OAuthHandler(apic,apisc)

auth.set_access_token(acc,acsc)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()

print(user.screen_name)

search="Verified at (Bed OR Blood OR Oxygen OR Fabiflu OR Plasma OR ICU OR Tocilizumab OR Ventilator OR Emergency OR Plasma OR donor OR verified OR needed OR available OR SOS) min_faves:3 min_retweets:5 -filter:replies"
nrtweets=500

count=0
for tweet in tweepy.Cursor(api.search,search).items(nrtweets):
    try:
        print("tweet retweeted",count)
        count=count+1
        tweet.retweet()
        time.sleep(30)
        ctr=str(count)
        cnt.truncate() 
        cnt.write(ctr)
        print("RETWEETED:",count)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

#api.update_status("THIS BOT HAD RETWEETED 800+ TWEETS DURING THE TIMES OF HELP , BUT AS THE FREQUENCY OF TWEETS FOR RESOURCES DECREASED THIS BOT WAS SHUT ! ")

ctr=str(count)

cnt.truncate() 

cnt.write(ctr)



