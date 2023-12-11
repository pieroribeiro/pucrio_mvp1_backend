from sqlalchemy.exc import IntegrityError
from datetime import datetime

from app.helpers.logger import logger
from app.schemas.messages.generic_message_schema import GenericMessageSchema
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.products.search_product_schema import SearchProductSchema
from app.schemas.products.create_product_schema import CreateProductSchema
from app.models import Session, Products
from app.openapi_tags.products import Tag_Product
from app import app

# Route: Update Product
@app.put("/product/<int:id>", tags = [Tag_Product], responses={"201": GenericMessageSchema, "404": GenericErrorSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def update_product(path: SearchProductSchema, form: CreateProductSchema):
    """
    Update Product
    """
    try:
        product_id = path.id
        session = Session()
        product = session.query(Products).filter(Products.id == product_id).first()
            
        if not product:
            error_msg = f"Product not found to update!"
            logger.warning(error_msg)
            return {"message": error_msg}, 404
        else:
            product.name = form.name
            product.value = form.value
            product.updated_at = datetime.now()
            session.commit()
            return {"message": f"Product '{product_id} updated'"}, 201
        
    except IntegrityError as e:
        error_msg = "Product with same name already exists in database"
        logger.warning(f"Error to update product '{product_id}', {error_msg}")

        return {"message": error_msg}, 409
    
    except Exception as e:
        error_msg = f"Not was possible to get the products from database"
        logger.warning(f"{error_msg}, {e}")

        return {"message": error_msg}, 500
