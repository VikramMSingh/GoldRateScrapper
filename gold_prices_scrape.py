import requests
from bs4 import BeautifulSoup
from csv_writer import write_data
from datetime import date
today_date=date.today()
d1=today_date.strftime("%d-%m-%Y")
url="https://www.bankbazaar.com/gold-rate-mumbai.html"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
strong=soup.find('strong',class_="bigfont")
price_22=strong.text[3:]
price_22=price_22.replace(',','')
price_22=int(price_22)*10
filename="gold_rates.csv"
write_data(filename,price_22,d1)
