from sqlalchemy.exc import IntegrityError

from app.helpers.logger import logger
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.sales.list_sales_schema import ListSalesSchema
from app.schemas.sales.show_sales import show_sales
from app.models import Session, Sales
from app.openapi_tags.sales import Tag_Sales
from app import app

# Route: GET All Products
@app.get("/sales/", tags = [Tag_Sales], responses={"200": ListSalesSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def get_sales():
    """
    Return all sales from database
    """
    try:
        session = Session()
        sales = session.query(Sales)
            
        if not sales:
            error_msg = f"Sales not found in database!"
            logger.warning(error_msg)
            return {"mesage": error_msg}, 404
        else:
            return show_sales (sales), 200
    
    except IntegrityError as e:
        logger.warning(e)

        return {"message": error_msg}, 409
    
    except Exception as e:
        error_msg = f"Not was possible to get the sales from database"
        logger.warning(e)

        return {"message": error_msg}, 500
