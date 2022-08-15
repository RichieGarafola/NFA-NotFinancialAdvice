import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import re
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import snscrape.modules.twitter as sntwitter

nltk.download('vader_lexicon')


st.title("Twitter NLP Scraper")
# Get user input
query = st.sidebar.text_input("Search word: ", value="AAPL")
df=pd.DataFrame()

# As long as the query is valid (not empty or equal to '#')...
if query != '':
    number_of_tweets = st.sidebar.text_input("Enter the number of tweets you want to Analyze: ",  value=100)
    if number_of_tweets != '' :
        number_of_days = st.sidebar.text_input("Enter the number of days you want to Scrape Twitter for: ", value=21)
        if number_of_days != '':
                #Create a list to append tweet data
                tweets_list = []
                now = dt.date.today()
                now = now.strftime('%Y-%m-%d')
                yesterday = dt.date.today() - dt.timedelta(days = int(number_of_days))
                yesterday = yesterday.strftime('%Y-%m-%d')
                for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query + ' lang:en since:' +  yesterday + ' until:' + now + ' -filter:links -filter:replies').get_items()):
                    if i > int(number_of_tweets):
                        break
                    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.username])

                # Create a dataframe using the tweets list above 
                df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

                st.write(df)

# Create a function to clean the tweets
def cleanTxt(text):
    text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
    text = re.sub('#', '', text) # Removing '#' hash tag
    text = re.sub('RT[\s]+', '', text) # Removing RT
    text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
    return text
df["Text"] = df["Text"].apply(cleanTxt)

# Sentiment Analysis
def percentage(part,whole):
    return 100 * float(part)/float(whole)

# Initialize Values
positive = 0
negative = 0
neutral = 0
sentiment = 0

# Initialize open buckets as holder for list
tweet_list1 = []
neutral_list = []
negative_list = []
positive_list = []
sentiment_list = []

# Iterating over the tweets in the dataframe
for tweet in df['Text']:
    tweet_list1.append(tweet)
    analyzer = SentimentIntensityAnalyzer().polarity_scores(tweet)
    neg = analyzer['neg']
    neu = analyzer['neu']
    pos = analyzer['pos']
    comp = analyzer['compound']

    if neg > pos:
        # append the tweet that satisfies 'negative_list' conditions
        negative_list.append(tweet)
        #increases the count by 1
        negative += 1 
         # if sentiment is negative, call it -1 and append it to the sentiment_list
        sentiment_list.append(-1)
        sentiment += 1
    elif pos > neg: 
        # append the tweet that satisfies 'positive_list' conditions
        positive_list.append(tweet)
        #increase the count by 1
        positive += 1 
         # if sentiment is positive, call it 1 and append it to the sentiment_list
        sentiment_list.append(1)
        sentiment += 1
    elif pos == neg:
        # append the tweet that satisfies 'neutral_list' conditions
        neutral_list.append(tweet) 
        #increase the count by 1 
        neutral += 1 
        

                
# Percent Positive
positive = percentage(positive, len(df)) 
# Percent Negative 
negative = percentage(negative, len(df)) 
# Percent Neutral
neutral = percentage(neutral, len(df))   

#Convert the lists to pandas dataframe 'tweet_list1', 'neutral_list', 'negative_list', 'positive_list'
tweet_list1 = pd.DataFrame(tweet_list1)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
#use len function to count lists. 
st.write("Since " + number_of_days + " days, there have been", len(tweet_list1) ,  "tweets on " + query,'\n*')
st.write("Positive Sentiment:", '%.2f' % len(positive_list),'\n*')
st.write("Neutral Sentiment:", '%.2f' % len(neutral_list), '\n*')
st.write("Negative Sentiment:", '%.2f' % len(negative_list), '\n*')

#Create the PieCart
labels = ['Positive ['+str(round(positive))+'%]' , 'Neutral ['+str(round(neutral))+'%]','Negative ['+str(round(negative))+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for keyword= "+query+"" )
plt.axis('equal')
plt.show()
st.pyplot(plt)

# word cloud visualization
def word_cloud(text):
    stopwords = set(STOPWORDS)
    allWords = ' '.join([twts for twts in text])
    wordCloud = WordCloud(background_color='black',width = 1600, height = 800,stopwords = stopwords,min_font_size = 20,max_font_size=150,colormap='prism').generate(allWords)
    fig, ax = plt.subplots(figsize=(20,10), facecolor='k')
    plt.imshow(wordCloud)
    ax.axis("off")
    fig.tight_layout(pad=0)
    plt.show()
    st.pyplot(plt)

st.write('Wordcloud for ' + query)
word_cloud(df['Text'].values)




