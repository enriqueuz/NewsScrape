import os, re

# Create directories for each day
def create_dir(news_list):
    for news in news_list:
        news_date = re.sub("[:]", "-", (news.pubDate.text))    
        date = news_date[0:16]        
        try:
            news_directory = "news/" + date            
            os.mkdir(news_directory)
        except FileExistsError:
            pass
    return date

