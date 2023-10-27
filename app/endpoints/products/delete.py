from flask_openapi3 import Tag

from app.helpers.logger import logger
from app.schemas.products.search_product_schema import SearchProductSchema
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.messages.generic_message_schema import GenericMessageSchema
from app.models import Session, Product
from app import app

# tags of routes
tag_product  = Tag(name="Product", description="CRUD of Products")

# Route: Delete Product
@app.delete("/product/", tags = [tag_product], responses={"201": GenericMessageSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def delete_product(query: SearchProductSchema):
    """
    Delete Product
    """
    try:
        product_id = query.id
        session = Session()
        product = session.query(Product).filter(Product.id == product_id)
            
        if not product.first():
            error_msg = f"Product not found to delete!"
            logger.warning(error_msg)
            return {"mesage": error_msg}, 404
        else:
            product.delete()
            session.commit()
            return {"mesage": f"Product '{product_id} deleted'"}, 200
    
    except Exception as e:
        error_msg = f"Not was possible to find the product from database to delete"
        logger.warning(f"{error_msg}, {e}")

        return {"message": error_msg}, 500
