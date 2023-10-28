from flask_openapi3 import Tag

from app.helpers.logger import logger
from app.schemas.sells.create_sell_schema import CreateSellSchema
from app.schemas.sells.view_sell_schema import ViewSellSchema
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.sells.show_sell import show_sell
from app.models import Session, Sells
from app import app

# tags of routes
tag_sells  = Tag(name="Sells", description="CRUD of Sells")

# Route: Create Product
@app.post("/sells/", tags = [tag_sells], responses={"201": ViewSellSchema, "500": GenericErrorSchema})
def create_product(form: CreateSellSchema):
    """
    Create a new sell in Database
    Return created sell
    """

    try:
        sell = Sells(product_id=form.product_id, product_value=form.product_value)

        session = Session()
        session.add(sell) 
        session.commit()

        logger.debug(f"The sell '{sell.id}' has been saved on database!")

        return show_sell(sell), 201

    except Exception as e:
        error_msg = "Not was possible to save the sell into database"
        logger.warning(f"Error to add product '{sell.id}', {error_msg}")

        return {"message": error_msg}, 500
