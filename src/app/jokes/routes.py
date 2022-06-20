from flask import Flask, jsonify
from . import jokes
from .utils.jokesFunctions import *

@jokes.route("/jokes", methods=['GET'])
@jokes.route("/jokes/", methods=['GET'])
def Jokes():
    url = jokesRandom()
    return jsonify({"message":jokesResponse(url)})

@jokes.route("/jokes/<name>", methods=['GET'])
def JokesId(name):
    url = jokesSelect(name)
    return jsonify({"message":jokesResponse(url)})
