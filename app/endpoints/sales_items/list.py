from sqlalchemy.exc import IntegrityError

from app.helpers.logger import logger
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.sales_items.list_sales_items_schema import ListSalesItemsSchema
from app.schemas.sales_items.search_sales_items_schema import SearchSalesItemsSchema
from app.schemas.sales_items.show_sale_items import show_sale_items
from app.models import Session, Sales_Items
from app.openapi_tags.sales_items import Tag_Sales_Items
from app import app

# Route: GET All Products
@app.get("/sales_items/<int:id>", tags = [Tag_Sales_Items], responses={"200": ListSalesItemsSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def get_sales_items(path: SearchSalesItemsSchema):
    """
    Return all sales from database
    """
    try:
        sale_id = path.id

        session = Session()
        sale_items = session.query(Sales_Items).filter(Sales_Items.sale_id == sale_id).first()
            
        if not sale_items:
            error_msg = f"Items of Sale '{sale_id}' not found in database!"
            logger.warning(f"Error on search Sale Items in database, {error_msg}")
            return {"mesage": error_msg}, 404
        else:
            return show_sale_items (sale_items), 200    
    except Exception as e:
        error_msg = f"Not was possible to get the sales from database"
        logger.warning(f"{error_msg}, {e}")

        return {"message": error_msg}, 500
