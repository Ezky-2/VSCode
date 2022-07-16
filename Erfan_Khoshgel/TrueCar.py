from bs4 import BeautifulSoup
from requests import get
import re

def search_truecar(car_berand:str):

    url = 'https://www.truecar.com/used-cars-for-sale/listings/%s/?sort[]=best_match'

    reader = get(url % car_berand)

    soup = BeautifulSoup(reader.text , 'html.parser')

    cars = soup.find_all('div' , {"data-test":"cardContent"})

    counter = 0
    paian_list = None

    for car in cars:

        if counter == 20:
            break

        car = car.text

        x = re.findall(r'Sponsored(\d\d\d\d)' , car)
        if x == []:
            x = re.findall(r'(\d\d\d\d) %s' %(car_berand.title()) , car)
            x = x[0]
        else:
            x = x[0]
        sal_sakht = int(x)

        x = re.findall(r'\$(\d+\,\d\d\d)' , car)
        x = x[0]
        ghimat = int(re.sub(r'\,' , '' , x))

        car = re.sub(r'\$(\d+\,\d\d\d)' , ' ' , car)

        x = re.findall(r'(\d+\,\d\d\d)\s*miles' , car)
        x = x[0]
        karkard = int(re.sub(r'\,' , '' , x))

        x = re.findall(r'miles(.+\,\s*\w\w)' , car)
        x = x[0]
        mahal_forosh = x

        x = re.findall(r'\W\W\w+ exterior' , car)
        x = x[0]
        exterior = x[2:]

        x = re.findall(r' (\w+) interior' , car)
        x = x[0]
        interior = x

        x = re.findall(r'interior(\w\w|\d+) (accident)|(accidents)' , car)
        x = x[0][0]
        numbar_accidents = x

        x = re.findall(r'(accident)|(accidents), (\d+) Owner' , car)
        x = x[0][2]
        number_owners = x

        x = re.findall(r'(Owners)|(Owner),\s*(\w+)\s*use' , car)
        x = x[0][2]
        how_to_use = x

        x = re.findall(r'MPG: (\d\d\-\d\d)' , car)
        x = x[0]
        mpg = x

        x = re.findall(r'Engine: .+?\,' , car)
        x = x[0]
        engine = x

        x = re.findall(r'Transmission: (\w+),' , car)
        x = x[0]
        transmission = x

        x = re.findall(r'VIN\: (.+)' , car)
        x = x[0]
        vin = x

        last = [sal_sakht, ghimat, karkard, mahal_forosh, exterior, interior, numbar_accidents, number_owners, how_to_use, mpg, engine, transmission, vin]

        if paian_list == None:
            paian_list = []

        paian_list.extend(last)

        counter += 1

    return paian_list

print (search_truecar('audi'))
