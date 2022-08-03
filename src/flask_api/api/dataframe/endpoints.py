"""API endpoint definitions for /auth namespace."""
from http import HTTPStatus
from flask import render_template
from flask_restx import Namespace, Resource
from src.flask_api.api.dataframe.business import retrieve_activity
from IPython.display import HTML

dataframe_ns = Namespace(name="dataframe", validate=True)


@dataframe_ns.route("/alive", endpoint="alive")
class edgeworks(Resource):
    @dataframe_ns.response(int(HTTPStatus.OK), "OK.")
    def get(self):
        """return server alive"""
        return "alive"
    
@dataframe_ns.route("/dataframe", endpoint="dataframe")
class edgeworks(Resource):
    @dataframe_ns.response(int(HTTPStatus.OK), "Data Valid.")
    @dataframe_ns.response(int(HTTPStatus.BAD_REQUEST), "Bad Parsing.")
    def get(self):
        """Return Value of Inventory Activity"""
        path_file = "src/flask_api/models/inventory_activity.csv"
        df = retrieve_activity(path_file)
        print(df)
  
