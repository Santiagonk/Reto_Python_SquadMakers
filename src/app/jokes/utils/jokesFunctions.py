import requests
import random
import json

def jokesRandom():
    dad_url = "https://icanhazdadjoke.com/slack"
    chuck_url = "https://api.chucknorris.io/jokes/random"

    url = random.choice([dad_url, chuck_url])

    return url

def jokesSelect(name):
    dad_url = "https://icanhazdadjoke.com/slack"
    chuck_url = "https://api.chucknorris.io/jokes/random"

    if name.lower() == "chuck":
        url = chuck_url
    elif name.lower() == "dad":
        url = dad_url
    else:
        url = "Word not found"

    return url

def jokesResponse(url):
    dad_url = "https://icanhazdadjoke.com/slack"
    chuck_url = "https://api.chucknorris.io/jokes/random"
    try:
        r = requests.get(url)
        r = r.json()
    except:
        pass

    if url == dad_url:
        r = r["attachments"][0]["text"]
    elif url == chuck_url:
        r =  r["value"]
    else:
        r = url

    return r