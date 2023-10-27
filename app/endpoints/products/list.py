from flask_openapi3 import Tag

from sqlalchemy.exc import IntegrityError
from datetime import datetime

from app.helpers.logger import logger
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.products.list_products_schema import ListProductsSchema
from app.schemas.products.show_products import show_products
from app.models import Session, Product
from app import app

# tags of routes
tag_product  = Tag(name="Product", description="CRUD of Products")

# Route: GET All Products
@app.get("/products", tags = [tag_product], responses={"200": ListProductsSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def get_products():
    """
    Return all products from database
    """
    try:
        session = Session()
        products = session.query(Product)
            
        if not products:
            error_msg = f"Products not found in database!"
            logger.warning(error_msg)
            return {"mesage": error_msg}, 404
        else:
            return show_products (products), 200
    
    except Exception as e:
        error_msg = f"Not was possible to get the products from database"
        logger.warning(f"{error_msg}, {e}")

        return {"message": error_msg}, 500
