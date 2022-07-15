import re

car = 'Sponsored2019 Audi Q8PremiumFair PriceAt or near avg. list price 20,532 milesHighland Park, ILBlack exterior, Black interiorNo accidents, 1 Owner, Personal useCertified Pre-OwnedMPG: 17-22, Engine: 3.0L V-6 Gas Turbocharged, Transmission: Automatic, AWDVIN: WA1AVAF19KD010866'

# car = 'Sponsored2013 Audi S4Premium Plus Sedan S tronicGreat Price$617 off avg. list price 78,604 milesClayton, IDWhite exterior, Black interiorNo accidents, 3 Owners, Personal useMPG: 18-28, Engine: 3.0L V-6 Gas Supercharged, Transmission: Automatic, AWDVIN: WAUBGAFL7DA192512'

x = re.findall(r'(Owners)|(Owner),\s*(\w+)\s*useMPG:' , car)

# x = x[0]
print (x)
