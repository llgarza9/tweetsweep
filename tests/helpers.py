#transforms datetime into a more analysis-friendly format
def convert_datetime(datetime_value):
    import datetime
    datetime_entries={'year':'%Y','day':'%d','month':'%m','hour':'%H','minute':'%M'}
    date={}
    for key,val in datetime_entries.items():
        date[key]=datetime_value.strftime(val)
    return date

#Collects hashtags for a tweet from the returned tweepy data
def isolate_hashtags(tweet):
    hashtags=[]
    for hashtag in tweet.entities['hashtags']:
        hashtags.append(hashtag['text'])
    return hashtags

#Collects mentions for a tweet from the returned tweepy data
def isolate_mentions(tweet):
    mentions=[]
    for mention in tweet.entities['user_mentions']:
        mentions.append(mention['screen_name'])
    return mentions

#Collects urls for a tweet from the returned tweepy data. Because tweepy did not appear to capture all the urls for a tweet sometimes, I also equipped this function to double check for urls in the tweet text that were not captured by tweepy.
def isolate_urls(tweet):
    urls=[]
    for url in tweet.entities['urls']:
        urls.append(url['url'])
    import re
    extra_urls=re.compile('https://[^\s]+')
    found_extra=re.findall(extra_urls,tweet.text)
    for url in found_extra:
        if url not in urls:
            urls.append(url)
    return urls

#Returns a tweet text in all lowercase and with punctuation removed
def text_clean(tweet_text):
    import string
    text=tweet_text
    text=text.lower()
    for ch in string.punctuation:
        text=text.replace(ch,"")
    text=text.strip()
    return text
