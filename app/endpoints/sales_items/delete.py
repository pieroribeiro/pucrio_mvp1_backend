from app.helpers.logger import logger
from app.schemas.sales_items.delete_sales_items_schema import DeleteSalesItemsSchema
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.messages.generic_message_schema import GenericMessageSchema
from app.models import Session, Sales_Items
from app.openapi_tags.sales_items import Tag_Sales_Items
from app import app

# Route: Delete Product
@app.delete("/sales_items/<int:sale_id>/<int:product_id>", tags = [Tag_Sales_Items], responses={"201": GenericMessageSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def delete_sale_items(path: DeleteSalesItemsSchema):
    """
    Delete Sale Item
    """
    try:
        sale_id = path.sale_id
        product_id = path.product_id

        session = Session()
        sale = session.query(Sales_Items).filter(Sales_Items.sale_id == sale_id, Sales_Items.product_id == product_id)
            
        if not sale.first():
            return {"mesage": f"Product '{product_id}' of sale '{sale_id}' not found on database!"}, 404
        else:
            sale.delete()
            session.commit()
            return {"mesage": f"Product '{product_id}' of sale '{sale_id}' deleted'"}, 200
    
    except Exception as e:
        error_msg = f"Not was possible to find the sale item from database to delete"
        logger.warning(e)

        return {"message": error_msg}, 500
