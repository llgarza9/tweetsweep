#Importing needed packages for program
import helpers as h
import tweepy as tw
import api
import json
from collections import Counter

#Setting up api authorization with values from the api.py file
auth = tw.OAuthHandler(api.consumer_key, api.consumer_secret)
auth.set_access_token(api.access_token, api.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#Defining values for tweet query
hashtag = "[#yourhashtag]" + " -filter:retweets" #Collects tweets that all have the specified hashtag excluding retweets
start_date = '[your date, ex: 2019-11-01]' #From what date onward do you want to collect tweets?
tweet_num='[number of tweets as int value]' #How many tweets do you want to collect?

#Running tweet query
tweets = tw.Cursor(api.search,
                   q=hashtag,
                   lang="en",
                   since=start_date).items(tweet_num)

#Setting up list for cleaned tweets
tweets_list=[]

#Extracting and cleaning tweet content collected from query
for tweet in tweets:
    tweet_content={}
    tweet_content['id']=tweet.id_str
    tweet_text=tweet.text
    tweet_content['date']=h.convert_datetime(tweet.created_at)
    tweet_content['hashtags']=h.isolate_hashtags(tweet)
    tweet_content['urls']=h.isolate_urls(tweet)
    tweet_content['mentions']=h.isolate_mentions(tweet)
    if len(tweet_content['hashtags'])>0:
        for hashtag in tweet_content['hashtags']:
            hashtag="#"+hashtag
            tweet_text=tweet_text.replace(hashtag,"")
    if len(tweet_content['urls'])>0:
        for url in tweet_content['urls']:
            tweet_text=tweet_text.replace(url,"")
    if len(tweet_content['mentions'])>0:
        for mention in tweet_content['mentions']:
            mention="@"+mention
            tweet_text=tweet_text.replace(mention,"")
    tweet_content['text']=h.text_clean(tweet_text)
    tweets_list.append(tweet_content)

#Renaming clean tweet collection to 'data'
data=tweets_list

#Creating lists for each variable of cleaned tweets
hashtags_list=[]
mentions_list=[]
text_list=[]
urls_list=[]
for record in data:
    for hashtag in record['hashtags']:
        hashtags_list.append(hashtag)
    for mention in record['mentions']:
        mentions_list.append(mention)
    for url in record['urls']:
        urls_list.append(url)
    text_data=record['text'].split()
    for word in text_data:
        text_list.append(word)

#Quick summary of collected tweet data via frequency of values for each variable.
hashtags_freq=Counter(hashtags_list)
mentions_freq=Counter(mentions_list)
text_freq=Counter(text_list)
urls_freq=Counter(urls_list)

#Save clean tweet data as a json file
with open('twitterdata.json','w', encoding='utf-8') as outfile_tweets:
    json.dump(tweets_list,outfile_tweets)
outfile_tweets.close()

#Save quick summary as txt file
outfile_counts = open('twitterdata_summary.txt','w', encoding = 'utf-8')
for item in [hashtags_freq,mentions_freq,text_freq,urls_freq]:
    print(item, file=outfile_counts)
outfile_counts.close()

