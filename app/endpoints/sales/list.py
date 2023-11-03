from flask_openapi3 import Tag

from sqlalchemy.exc import IntegrityError
from datetime import datetime

from app.helpers.logger import logger
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.sales.list_sales_schema import ListSalesSchema
from app.schemas.sales.show_sales import show_sales
from app.models import Session, Sales
from app import app

# tags of routes
tag_sales  = Tag(name="Sales", description="CRUD of Sales")

# Route: GET All Products
@app.get("/products/", tags = [tag_sales], responses={"200": ListSalesSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def get_sales():
    """
    Return all sales from database
    """
    try:
        session = Session()
        sales = session.query(Sales)
            
        if not sales:
            error_msg = f"Sales not found in database!"
            logger.warning(error_msg)
            return {"mesage": error_msg}, 404
        else:
            return show_sales (sales), 200
    
    except Exception as e:
        error_msg = f"Not was possible to get the sales from database"
        logger.warning(f"{error_msg}, {e}")

        return {"message": error_msg}, 500
