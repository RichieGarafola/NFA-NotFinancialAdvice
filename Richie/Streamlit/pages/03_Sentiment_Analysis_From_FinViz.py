import streamlit as st
# get data
from urllib.request import urlopen, Request

# parse data from FinViz 
from bs4 import BeautifulSoup
import os
# manipulate and store the data in DataFrames
import pandas as pd
# plot the sentiment on a chart
import matplotlib.pyplot as plt

# NLTK VADER for sentiment analysis on the news headlines
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# take the raw part of the url, we will append the ticker to the end of the link to pull up its data
# Extract data from finviz use the raw url.
finwiz_url = 'https://finviz.com/quote.ashx?t='

tickers = ('AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS',	'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH','CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW')
tickers_dropdown = st.selectbox('Choose a stock ticker', tickers)

# Initiate an empty dictionary to hold the news tables from website
news_tables = {}
tickers = [tickers_dropdown]

for ticker in tickers:
    url = finwiz_url + ticker
    req = Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}) 
    response = urlopen(req)    
    # Read the contents of the file into 'html'
    html = BeautifulSoup(response)
    # Find 'news-table' in the Soup and load it into 'news_table'
    news_table = html.find(id='news-table')
    # Add the table to our dictionary
    news_tables[ticker] = news_table

    
# <td> tag defines the standard cells in the table which are displayed as normal-weight, left-aligned text. 
# <tr> tag defines the table rows.

# Read headlines for 'stock' 
stock = news_tables[tickers_dropdown]
# Get all the table rows tagged in HTML with <tr> into 'stock_tr'
stock_tr = stock.findAll('tr')

#Create a list to append the titles
title_list = []
        
# The enumerate() function takes a collection and returns it as an enumerate object.
for index, table_row in enumerate(stock_tr):
    # Read the text of the element 'a' (Anchor tag) into 'title' 
    title = table_row.a.text
    # Read the text of the element 'td' into 'timestamp' for the timestamp
    timestamp = table_row.td.text.split()
    
    # if the length of 'timestamp' is 1, load 'time' as the only element
    if len(timestamp) == 1:
        time = timestamp[0]
            
    # else load 'date' as the 1st element and 'time' as the second    
    else:
        date = timestamp[0]
        time = timestamp[1]
    ticker = tickers
            
    # Append the title and timestamp to list format. 
    title_list.append([tickers, date, time, title])
    # Create a dataframe using the 'title_list'
    finviz_headlines = pd.DataFrame(title_list, columns=[['ticker', 'date', 'time', 'title']])
    
# Percentage 
def percentage(part,whole):
    return 100 * float(part)/float(whole)


# Initialize Values
positive = 0
negative = 0
neutral = 0


# Initialize open buckets as holder for list
title_list = []
neutral_list = []
negative_list = []
positive_list = []

# Iterating over the titles in the dataframe
for title in finviz_headlines['title']:
    title_list.append(title)
    analyzer = SentimentIntensityAnalyzer().polarity_scores(title)
    neg = analyzer['neg']
    neu = analyzer['neu']
    pos = analyzer['pos']
    comp = analyzer['compound']

    if neg > pos:
        # append the headline that satisfies 'negative_list' conditions
        negative_list.append(title)
        #increases the count by 1
        negative += 1 
         # if sentiment is negative, call it -1 and append it to the sentiment_list
        sentiment_list.append(-1)
        sentiment += 1
    elif pos > neg: 
        # append the tweet that satisfies 'positive_list' conditions
        positive_list.append(title)
        #increase the count by 1
        positive += 1 
         # if sentiment is positive, call it 1 and append it to the sentiment_list
        sentiment_list.append(1)
        sentiment += 1
    elif pos == neg:
        # append the tweet that satisfies 'neutral_list' conditions
        neutral_list.append(title) 
        #increase the count by 1 
        neutral += 1 
               
# Percent Positive
positive = percentage(positive, len(finviz_headlines)) 
# Percent Negative 
negative = percentage(negative, len(finviz_headlines)) 
# Percent Neutral
neutral = percentage(neutral, len(finviz_headlines)) 

#Convert the lists to pandas dataframe 'title_list', 'neutral_list', 'negative_list', 'positive_list'
title_list = pd.DataFrame(title_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)

# print("Since " + number_of_days + " days, there have been", len(tweet_list1) ,  "tweets on " + query,'\n*')
print("Positive Sentiment:", '%.2f' % len(positive_list),'\n*')
print("Neutral Sentiment:", '%.2f' % len(neutral_list), '\n*')
print("Negative Sentiment:", '%.2f' % len(negative_list), '\n*')

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
