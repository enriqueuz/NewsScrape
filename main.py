import bs4, re, os, my_funcs, shutil
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Tuple with news rss links
news_urls = ("https://news.yahoo.com/rss/mostviewed", "https://news.google.com/news/rss")

#Check if 'news' directory exist
is_news_dir = os.path.isdir('./news')
if is_news_dir == False:
  print("Creating 'news' directory...")
  os.mkdir("news")

# Loop for each news server
for news_page in news_urls:
  Client=urlopen(news_page)
  xml_page=Client.read()
  Client.close()
  soup_page=BeautifulSoup(xml_page,"xml")
  news_list=soup_page.findAll("item")

  date = my_funcs.create_dir(news_list) 

# Give each news shortcut a name
  for news in news_list:  
     news_title = re.sub("[.^$*+?{[]||()/:,<>--'']", "", news.title.text)
     news_link = "URL = " + news.link.text

     #There was an error with very long titles
     try:
       f= open("news/" + date + "/" + news_title +".url","w+")
       f.write("[InternetShortcut]\n")
       f.write(news_link)
     except:
       print("The following new", news_title, " was not able to download")
       f= open("news/" + date + "/" + "EQUIS" +".url","w+")
       f.write("[InternetShortcut]\n")
       f.write(news_link)      
         

print("Opening directory...")
os.startfile("news")