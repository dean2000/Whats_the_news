import requests
from bs4 import BeautifulSoup
import smtplib
import ssl
import datetime

#extract the date from datetime.now method
current_date = (datetime.datetime.date(datetime.datetime.now()))
current_time = str(datetime.datetime.time(datetime.datetime.now()))[:8]
site_url = 'https://www.bbc.com/news'
html = requests.get(site_url)
soup = BeautifulSoup(html.text,"html.parser")

mail_contex = (f"\nHello, Those are the news for {current_date} on {site_url}:\nrelevance for {current_time}:\n\n")

#extract the titles by class name
titles = (soup.findAll("a",class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'))

for i in range(len(titles)): #iterates through all titles
		if ((titles[i].string)!=None):
			mail_contex += (f"[{i+1}.] ")
			#if there is non-english character it replace with ""
			mail_contex += (''.join([l if ord(l) < 128 else "" for l in(titles[i].string)]))
			mail_contex += '\n'

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as server:
	server.ehlo()  # Can be omitted
	server.starttls(context=context)
	server.ehlo()  # Can be omitted
	server.login("servicedeanm@gmail.com", "dean_dean_123")
	server.sendmail("servicedeanm@gmail.com", "deanmarkin3@gmail.com", mail_contex)
	server.quit()
