from bs4 import BeautifulSoup
from requests import get
from re import sub

reader = get('https://divar.ir/s/mashhad')

soup = BeautifulSoup(reader.text , 'html.parser')

vorodi = soup.find_all('div' , {'class':"kt-post-card__body"})

for har_tabligh in vorodi:
    har = har_tabligh.text
    if 'توافقی' in har:
        x = sub(r'توافقی' , ' ' , har).strip()
        print (sub(r'لحظاتی پیش در' , 'مکان:' , x).strip())
