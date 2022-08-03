"""API endpoint definitions for /auth namespace."""
from http import HTTPStatus
from flask import make_response, render_template
from flask_restx import Namespace, Resource
from src.flask_api.api.dataframe.business import retrieve_activity

headers = {'Content-Type': 'text/html'}
dataframe_ns = Namespace(name="dataframe", validate=True)

@dataframe_ns.route("/alive", endpoint="alive")
class edgeworks(Resource):
    @dataframe_ns.response(int(HTTPStatus.OK), "OK.")
    def get(self):
        """return server alive"""
        return "alive"
    
@dataframe_ns.route("/dataframe", endpoint="dataframe")
class edgeworks(Resource):
    @dataframe_ns.response(int(HTTPStatus.OK), "OK.")
    def get(self):
        """return value of inventory activity"""
        path_file = "src/flask_api/models/inventory_activity.csv"
        df = retrieve_activity(path_file)
        df.to_html(classes='data')
  
        return make_response(render_template("simple.html", tables=[df.to_html(classes='data')], titles=['Inventory Activity']),200, headers)