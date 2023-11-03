from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

app    = OpenAPI(__name__, info = Info(title="Product API", version="1.0.0"))
CORS(app)

from app.endpoints.products import create, delete, get, list, update
from app.endpoints.sales import create, delete, list
from app.endpoints.sales_items import create, delete, list

@app.errorhandler(404)
def endpoint_not_found(error):
    return {"message": "This endpoint is not available"}, 404

