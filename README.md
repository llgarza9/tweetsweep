# TweetSweep

## General Information:

### Description: 
: This is a python program designed to gather a specified number of tweets sharing the same specified hashtag, cleaning the data to produce a json file of each tweet's timestamp, text, mentions, urls, and additional hashtags, and quickly summarizing the data by frequency in a txt file. Program was created for the course "Foundations of Information Processing" at the University of Illinois at Urbana-Champaign in 2019.
### Author: 
: Livia Lee Garza, liviag2@illinois.edu
### Date Published:
: 2019-12-09

## Prerequisites:
* You will need API access for Twitter. You can learn more about how to apply [here](https://developer.twitter.com/)
* This program requires the following packages:
	* tweepy
	* datetime
	* json
	* re
	* string
	* collections
	While the latter five packages should be in the python standard library, tweepy needs to be downloaded either via PyPI or Github. [More information here](https://github.com/tweepy/tweepy)

## Running the Code:
1. Set up api.py file with api keys and tokens provided by Twitter.
2. In tweetsweep.py, specify the hashtag you would like to search by, since what date, and for how many tweets.
3. Run tweetsweep.py and result files will be returned in the tweetsweep directory.

