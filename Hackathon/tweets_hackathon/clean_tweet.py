import json
import re
import sys
import os
import re

def generateStopWordList():

    stopWords_dataset = "stopwords1.txt"

    stopWords = []

    try:
        fp = open(stopWords_dataset, 'r')
        line = fp.readline()
        while line:
            word = line.strip()
            stopWords.append(word)
            line = fp.readline()
        fp.close()
    except:
        print("ERROR: Opening File")

    return stopWords



def preprocessing(dataSet):

    processed_data = []

    stopWords = generateStopWordList()

    for i,tweet in enumerate(dataSet,1):
      if "http" in tweet:
            # urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)
            # print(i, urls,file=open("food_image_urls\\unhealthy_food_image_tweet.txt", "a"))
        temp_tweet = tweet
        tweet = re.sub('http\S+', " ", tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('@[^\s]+', '', tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('[\s]+', ' ', tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

        tweet = re.sub('[0-9]+', "", tweet)
        tweet.replace(temp_tweet, tweet)

        for sw in stopWords:
            if sw in tweet:
                tweet = re.sub(r'\b' + sw + r'\b' + " ", "", tweet)

        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('[^a-zA-z ]', "", tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('[\s]+', ' ', tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('http\S+', " ", tweet)
        tweet.replace(temp_tweet, tweet)


        tweet = tweet.strip()

        processed_data.append(tweet)

    return processed_data

positive_data = open("Cleaned_tweets1_opoid_drugs.txt",encoding="utf-8").readlines()
positive_data = preprocessing(positive_data)
pw = open("clean_tweets.txt","w")

for i in positive_data:
    pw.write(str(i))
    pw.write("\n")
pw.close()