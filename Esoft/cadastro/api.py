import requests, json

r = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio')
    nome1 = r.json()[0]
    nome2 = r.json()[1]
    nome3 = r.json()[2]
    resultado = nome1 + " " + nome2 + " " + nome3