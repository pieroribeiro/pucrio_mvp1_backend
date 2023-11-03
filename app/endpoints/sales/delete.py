from sqlalchemy.exc import IntegrityError

from app.helpers.logger import logger
from app.schemas.sales.search_sales_schema import SearchSalesSchema
from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.schemas.messages.generic_message_schema import GenericMessageSchema
from app.models import Session, Sales
from app.tags.sales import Tag_Sales
from app import app

# Route: Delete Product
@app.delete("/sales/<int:id>", tags = [Tag_Sales], responses={"201": GenericMessageSchema, "409": GenericErrorSchema, "500": GenericErrorSchema})
def delete_sale(path: SearchSalesSchema):
    """
    Delete Product
    """
    try:
        sale_id = path.id
        session = Session()
        sale = session.query(Sales).filter(Sales.id == sale_id)
            
        if not sale.first():
            error_msg = f"Sale not found to delete!"
            logger.warning(error_msg)
            return {"mesage": error_msg}, 404
        else:
            sale.delete()
            session.commit()
            return {"mesage": f"Sale '{sale_id} deleted'"}, 200
    
    except IntegrityError as e:
        logger.warning(e)

        return {"message": error_msg}, 409
    
    except Exception as e:
        error_msg = f"Not was possible to find the sale from database to delete"
        logger.warning(f"{error_msg}, {e}")

        return {"message": error_msg}, 500
