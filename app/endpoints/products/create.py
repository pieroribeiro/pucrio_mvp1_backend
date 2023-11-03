from sqlalchemy.exc import IntegrityError

from app.helpers.logger import logger
from app.schemas.products.create_product_schema import CreateProductSchema
from app.schemas.products.view_product_schema import ViewProductSchema
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.products.show_product import show_product
from app.models import Session, Product
from app.tags.products import Tag_Product
from app import app

# Route: Create Product
@app.post("/product/", tags = [Tag_Product], responses={"201": ViewProductSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def create_product(form: CreateProductSchema):
    """
    Create a new product in Database
    Return created product
    """

    try:
        product = Product(name=form.name, value=form.value)

        session = Session()
        session.add(product) 
        session.commit()

        logger.debug(f"The product '{product.name}' has been saved on database!")

        return show_product(product), 201
    
    except IntegrityError as e:
        error_msg = "Product with same name already exists in database"
        logger.warning(f"Error to add product '{product.name}', {error_msg}")

        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Not was possible to save the product into database"
        logger.warning(f"Error to add product '{product.name}', {error_msg}")

        return {"message": error_msg}, 500
