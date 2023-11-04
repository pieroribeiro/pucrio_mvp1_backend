from sqlalchemy.exc import IntegrityError

from app.helpers.logger import logger
from app.schemas.products.create_product_schema import CreateProductSchema
from app.schemas.products.view_product_schema import ViewProductSchema
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.products.show_product import show_product
from app.models import Session, Products
from app.openapi_tags.products import Tag_Product
from app import app

# Route: Create Product
@app.post("/product/", tags = [Tag_Product], responses={"201": ViewProductSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def create_product(form: CreateProductSchema):
    """
    Create a new product in Database
    Return created product
    """

    try:
        product = Products(name=form.name, value=form.value)

        session = Session()
        session.add(product) 
        session.commit()

        logger.debug(f"The product '{product.name}' has been saved on database!")

        return show_product(product), 201
    
    except IntegrityError as e:
        logger.warning(e)

        return {"message": "Product with same name already exists in database"}, 409

    except Exception as e:
        logger.warning(e)

        return {"message": "Not was possible to save the product into database"}, 500
