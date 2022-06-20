from flask import Blueprint

math = Blueprint('math', __name__)

from . import routes