from flask_openapi3 import Tag

from sqlalchemy.exc import IntegrityError
from datetime import datetime

from app.helpers.logger import logger
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.products.view_product_schema import ViewProductSchema
from app.schemas.products.search_product_schema import SearchProductSchema
from app.schemas.products.show_product import show_product
from app.models import Session, Product
from app import app

# tags of routes
tag_product  = Tag(name="Product", description="CRUD of Products")

# Route: GET Product by Id
@app.get("/product/", tags = [tag_product], responses={"200": ViewProductSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def get_product(query: SearchProductSchema):
    """
    Get a product from Database
    """

    try:
        product_id = query.id

        session = Session()
        product = session.query(Product).filter(Product.id == product_id).first()
            
        if not product:
            error_msg = f"Product '{product_id}' not found in database!"
            logger.warning(f"Error on search product in database, {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            return show_product (product), 200
    
    except Exception as e:
        error_msg = f"Not was possible to get the product '{product_id}' from database"
        logger.warning(f"{error_msg}, {e}")

        return {"message": error_msg}, 500
    