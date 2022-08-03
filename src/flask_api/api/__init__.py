"""API blueprint configuration."""
from flask import Blueprint
from flask_restx import Api

from src.flask_api.api.dataframe.endpoints import dataframe_ns

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    api_bp,
    version="1.0",
    title="Edgework Inventory Activity",
    description="Welcome to the Swagger UI documentation site!",
    doc="/ui",
)

api.add_namespace(dataframe_ns, path="/edgeworks")
