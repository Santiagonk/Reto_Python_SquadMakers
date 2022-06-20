from flask import Flask

def create_app(settings_module):
    print(f'Hi {settings_module}')
    app = Flask(__name__)

    from .main import main
    app.register_blueprint(main)

    from .jokes import jokes
    app.register_blueprint(jokes)

    from .math import math
    app.register_blueprint(math)

    return app