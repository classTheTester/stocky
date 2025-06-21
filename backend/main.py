from bs4 import BeautifulSoup
import requests
import google.generativeai as genai
import os



url = "https://www.nytimes.com/section/business?page=10"


def summarizeNews(url = url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    articles = doc.find_all(class_="css-1l4spti")

    article_information = ""
    for article in articles:
        article_information += ("(" + article.find_all('h3')[0].text + "," + article.find_all('p')[0].text + ")" + "||")


    genai.configure(api_key= "AIzaSyCH-DwXHz7n3tu4kYnMV7Gw52g5tF9BWpc")

    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = "The following contains tuples of titles and descriptions of articles. What stocks (along with their tickers) are the most impacted by these news" + article_information
    response = model.generate_content(prompt)
    return response.text

