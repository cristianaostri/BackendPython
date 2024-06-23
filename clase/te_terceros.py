import requests 
import pprint


consulta = requests.get('https://jsonplaceholder.typicode.com/users')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(consulta.json())