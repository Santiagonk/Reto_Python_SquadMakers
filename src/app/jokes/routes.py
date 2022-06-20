from flask import Flask, jsonify
from requests import request
from flask import request
from . import jokes
from .utils.jokesFunctions import *
from .models import Joke

@jokes.route("/jokes", methods=['GET'])
@jokes.route("/jokes/", methods=['GET'])
def Jokes():
    url = jokesRandom()
    return jsonify({"message":jokesResponse(url)})

@jokes.route("/jokes/<name>", methods=['GET', 'POST'])
def JokesId(name):
    url = jokesSelect(name)
    joke_text = jokesResponse(url)
    if request.method == 'POST':
        joke = Joke(description = joke_text, type = name)
        joke.save()
    return jsonify({"message":joke_text})

@jokes.route("/jokes/<name>/<int:number>", methods=['PUT'])
def putJoke(number, name):
    url = jokesSelect(name)
    joke_text = jokesResponse(url)
    joke = Joke.get_by_id(number)
    joke.update(description = joke_text)
    return jsonify({"message":joke.description})

@jokes.route("/jokes/<int:number>", methods=['DELETE'])
def deleteJoke(number):
    print(number)
    joke = Joke.get_by_id(number)
    joke.delete()
    return jsonify({"message":f'joke {number} delete'})
