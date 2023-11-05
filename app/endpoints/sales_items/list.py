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
@app.get("/sales_items/<int:sale_id>", tags = [Tag_Sales_Items], responses={"200": ListSalesItemsSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def get_sales_items(path: SearchSalesItemsSchema):
    """
    Return all sales from database
    """
    try:
        sale_id = path.sale_id

        session = Session()
        sale_items = session.query(Sales_Items).filter(Sales_Items.sale_id == sale_id)
            
        if not sale_items:
            return {"mesage": "Items of Sale '{sale_id}' not found in database!"}, 404
        else:
            return show_sale_items (sale_items), 200    
    except Exception as e:
        logger.warning(e)

        return {"message": "Not was possible to get the sales from database"}, 500
