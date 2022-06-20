from flask import Flask, jsonify
from . import math
from .utils.mathFunctions import *

@math.route("/numbers/<numbers>", methods = ['GET'])
def mathEndpointList(numbers):
    mcm = CalculateMCM(numbers)
    return jsonify({"message":mcm})


@math.route("/number/<number>", methods = ['GET'])
def mathEndpoint(number):
    return jsonify({"message":AddOne(number)})
