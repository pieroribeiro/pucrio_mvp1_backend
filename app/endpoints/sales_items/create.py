from sqlalchemy.exc import IntegrityError

from app.helpers.logger import logger
from app.schemas.sales_items.create_sale_item_schema import CreateSaleItemSchema
from app.schemas.sales_items.view_sales_items_schema import ViewSalesItemsSchema
from app.schemas.sales_items.show_sale_item import show_sale_item

from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.models import Session, Sales_Items
from app.openapi_tags.sales_items import Tag_Sales_Items
from app import app

# Route: Create Product
@app.post("/sales_items/<int:sale_id>/<int:product_id>", tags = [Tag_Sales_Items], responses={"201": ViewSalesItemsSchema, "500": GenericErrorSchema})
def create_sales_items(path: CreateSaleItemSchema):
    """
    Create a new sale items in Database
    Return created sale items
    """

    try:
        sale_id         = path.sale_id
        product_id      = path.product_id

        sale_item = Sales_Items(sale_id = sale_id, product_id = product_id)

        session = Session()
        session.add(sale_item) 
        session.commit()

        logger.debug(f"The item '{product_id}' of Sale '{sale_id}' has been saved on database!")

        return show_sale_item(sale_item), 201
    
    except IntegrityError as e:
        error_msg = "Product with same name already exists in database"
        logger.warning(e)

        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Not was possible to save the item of sale into database"
        logger.warning(e)

        return {"message": error_msg}, 500
