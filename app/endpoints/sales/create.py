from flask_openapi3 import Tag

from app.helpers.logger import logger
from app.schemas.sales import CreateSalesSchema, ViewSalesSchema, show_sales
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.models import Session, Sales
from app import app

# tags of routes
tag_sales  = Tag(name="Sales", description="CRUD of Sales")

# Route: Create Product
@app.post("/sales/", tags = [tag_sales], responses={"201": ViewSalesSchema, "500": GenericErrorSchema})
def create_product(form: CreateSalesSchema):
    """
    Create a new sales in Database
    Return created sales
    """

    try:
        sales = Sales(product_id=form.product_id, product_value=form.product_value)

        session = Session()
        session.add(sales) 
        session.commit()

        logger.debug(f"The sell '{sales.id}' has been saved on database!")

        return show_sales(sales), 201

    except Exception as e:
        error_msg = "Not was possible to save the sell into database"
        logger.warning(f"Error to add product '{sales.id}', {error_msg}")

        return {"message": error_msg}, 500