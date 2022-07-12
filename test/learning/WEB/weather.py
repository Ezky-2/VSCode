import requests
import re

vorodi = requests.get('https://api.openweathermap.org/data/2.5/weather?q=mashhad,IR-09,364&appid=947370ca7842441ff0ea3684a74fb5c9')
vorodi = vorodi.json()

# x = re.search(r'weather\s*(.+)icon' , vorodi)

print (vorodi)
