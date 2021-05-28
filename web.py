from flask import Flask
from flask_cors import CORS
from api import production_api

def create_app():
  app = Flask(__name__)
  app.register_blueprint(production_api)
  CORS(app)

  return app