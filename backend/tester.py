from newsapi import NewsApiClient
import os
from datetime import datetime, timedelta
import google.generativeai as genai


current_date = datetime.now()

one_week_ago = current_date - timedelta(days=3)


formatted_current_date = current_date.strftime("%Y-%m-%d")
formatted_one_week_ago = one_week_ago.strftime("%Y-%m-%d")




newsapi = NewsApiClient(api_key="e851fad21abe4907b90fc29f9f925796")

all_articles = newsapi.get_everything(language='en',
                                      domains='wired.com,wsj.com,washingtontimes.com,time.com,usatoday.com/news, huffingtonpost.com, theglobeandmail.com, politico.com, nbcnews.com, foxnews.com, bloomberg.com, nytimes.com',
                                      sort_by='relevancy',
                                      from_param=f"{formatted_one_week_ago}",
                                      to=f"{formatted_current_date}")

def getnews(all_articles = all_articles):

    article_information = ""
    for article in all_articles['articles']:
        article_information += "(" + article['title'] + "," + article['description'] + ")||" 


    genai.configure(api_key="AIzaSyCH-DwXHz7n3tu4kYnMV7Gw52g5tF9BWpc")

    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = "The following contains tuples of titles and descriptions of articles. What stocks (along with their tickers) are the most impacted by these news. return the answer in the following format \"(stock name| stock ticker| positive or negative impact| description)\". DO NOT GIVE ANY OTHER TEXT OR CHARACTERS OTHER THAN THIS FORMAT. " + article_information
    response = model.generate_content(prompt)

    return response.text