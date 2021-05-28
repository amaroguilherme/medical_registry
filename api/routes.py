from background.workflow import format_production
from api import production_api
from flask import jsonify

@production_api.route('/production', methods=['GET'])
def get_production():
  production = format_production()

  return jsonify({'result': production}), 200