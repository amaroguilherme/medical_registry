from flask import Flask
from api import production_api

def create_app():
  app = Flask(__name__)
  app.register_blueprint(production_api, url_prefix='/production')

  return app