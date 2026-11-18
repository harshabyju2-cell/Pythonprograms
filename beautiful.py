import requests
from bs4 import BeautifulSoup
import csv
url = "https://feeds.bbci.co.uk/news/technology/rss.xml"
response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")
with open("news.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "Date", "Category"])
    count = 0
    for news in soup.find_all("item"):
        headline = news.find("title")
        date = news.find("pubDate")
        category = news.find("category")
        if headline:
            title = headline.get_text(strip=True)
            pub_date = date.get_text(strip=True) if date else "N/A"
            cat = category.get_text(strip=True) if category else "Technology"
            writer.writerow([title, pub_date, cat])
            print("Headline:", title)
            print("Date:", pub_date)
            print("Category:", cat)
            print("-------------------")
            count += 1
        if count == 5:
            break
print("Total headlines extracted:", count)
print("Data saved successfully in news.csv")
