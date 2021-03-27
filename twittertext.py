import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob
    
def accessing(): 
        global api
        access_token = "# you have to acquire a access token from twitter using your own twitter account "
        access_token_secret = "#you have to acquire a access token pin from twitter using your own twitter account"
        consumer_key = "#you have to acquire access key for seeing another persons comments from twitter using your own twitter account"
        consumer_secret = "#you have to acquire access key pin for seeing another persons comments from twitter using your own twitter account"
        # attempt authentication 
        try: 
            # create OAuthHandler object 
            auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            api = tweepy.API(auth) 
        except: 
            print("Error: Authentication Failed")
def clean_tweet(tweet): 
            ''' 
            Utility function to clean tweet text by removing links, special characters 
            using simple regex statements. 
            '''
            return (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()))
def get_tweet_sentiment(tweet): 
            ''' 
            Utility function to classify sentiment of passed tweet 
            using textblob's sentiment method 
            '''
            # create TextBlob object of passed tweet text 
            analysis = TextBlob(clean_tweet(tweet)) 
            # set sentiment 
            if analysis.sentiment.polarity > 0: 
                return 'positive'
            elif analysis.sentiment.polarity == 0: 
                return 'neutral'
            else: 
                return 'negative'
    
def get_tweets(query, count = 10): 
            ''' 
            Main function to fetch tweets and parse them. 
            '''
            accessing()
            # empty list to store parsed tweets 
            tweets = []
            # 200 tweets to be extracted 
            
      
            try: 
                # call twitter api to fetch tweets 
                fetched_tweets =api.search(q = query, count = count) 
      
                # parsing tweets one by one 
                for tweet in fetched_tweets: 
                    # empty dictionary to store required params of a tweet 

                    parsed_tweet = {} 
      
                    # saving text of tweet 
                    parsed_tweet['text'] = tweet.text 
                    # saving sentiment of tweet 
                    parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text) 
      
                    # appending parsed tweet to tweets list 
                    if tweet.retweet_count > 0: 
                        # if tweet has retweets, ensure that it is appended only once 
                        if parsed_tweet not in tweets: 
                            tweets.append(parsed_tweet) 
                    else: 
                        tweets.append(parsed_tweet) 
      
                # return parsed tweets 
                return tweets 
      
            except tweepy.TweepError as e: 
                # print error (if any) 
                print("Error : " + str(e)) 
      
def main1(a): 
        global ptweets,ntweets,netweets,p,n,ne
        # creating object of TwitterClient Class 
        #api = TwitterClient() 
        # calling function to get tweets 
        tweets = get_tweets(query = a, count = 200) 
      
        # picking positive tweets from tweets 
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
        # percentage of positive tweets 
        
        print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
        # picking negative tweets from tweets 
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
        # percentage of negative tweets 
        print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
        # percentage of neutral tweets 
        print(len(tweets))
        netweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
        print("Neutral tweets percentage: {} % ".format(100*len(netweets)/len(tweets))) 
      
        # printing first 5 positive tweets 
        print("\n\nPositive tweets:") 
        for tweet in ptweets[:10]: 
            print(tweet['text']) 
      
        # printing first 5 negative tweets 
        print("\n\nNegative tweets:") 
        for tweet in ntweets[:10]: 
            print(tweet['text'])
        # printing first 5 neutral tweets
        print("\n\nNeutral tweets:") 
        for tweet in netweets[:10]: 
            print(tweet['text'])
        p=100*len(ptweets)/len(tweets)
        n=100*len(ntweets)/len(tweets)
        ne=100*len(netweets)/len(tweets)
main1("iamsrk")   

