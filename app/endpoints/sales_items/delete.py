from flask_openapi3 import Tag

from app.helpers.logger import logger
from app.schemas.sales_items.search_sales_items_schema import SearchSalesItemsSchema
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.messages.generic_message_schema import GenericMessageSchema
from app.models import Session, Sales_Items
from app.tags.sales_items import Tag_Sales_Items
from app import app

# Route: Delete Product
@app.delete("/sales_items/<int:id>", tags = [Tag_Sales_Items], responses={"201": GenericMessageSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def delete_sale_items(path: SearchSalesItemsSchema):
    """
    Delete Sale Item
    """
    try:
        sale__item_id = path.id
        session = Session()
        sale = session.query(Sales_Items).filter(Sales_Items.id == sale__item_id)
            
        if not sale.first():
            error_msg = f"Sale item not found to delete!"
            logger.warning(error_msg)
            return {"mesage": error_msg}, 404
        else:
            sale.delete()
            session.commit()
            return {"mesage": f"Sale item '{sale__item_id} deleted'"}, 200
    
    except Exception as e:
        error_msg = f"Not was possible to find the sale item from database to delete"
        logger.warning(f"{error_msg}, {e}")

        return {"message": error_msg}, 500
