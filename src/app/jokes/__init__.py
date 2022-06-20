from flask import Blueprint

jokes = Blueprint('jokes', __name__)

from . import routes