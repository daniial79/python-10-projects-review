import time
import datetime
import yagmail
import pandas
from news import NewsFeed, to_email_body


while True:
    if datetime.datetime.now().hour == 6 and datetime.datetime.now().minute == 00: 
        df = pandas.read_excel("people.xlsx")
        email = yagmail.SMTP(user="<username>@gmail.com", password="<password>")

        today = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        
        for index, row in df.iterrows():
            news_feed = NewsFeed(interest=row["interest"]
                                 , from_date=yesterday, 
                                 to_date=today, 
                                 language=row["language"]
                                )
            
            email.send(to=row["email"],
                    subject=f"Your {row["interest"]} news for today!",
                    contents=f"Hi {row["name"]}.\n see what's on about {row["interest"]} today!\n {to_email_body(news_feed.get())}")
            
    time.sleep(60)