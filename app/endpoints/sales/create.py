from sqlalchemy.exc import IntegrityError

from app.helpers.logger import logger
from app.schemas.sales.view_sales_schema import ViewSalesSchema
from app.schemas.sales.show_sale import show_sale

from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.models import Session, Sales
from app.tags.sales import Tag_Sales
from app import app

# Route: Create Product
@app.post("/sales/", tags = [Tag_Sales], responses={"201": ViewSalesSchema, "500": GenericErrorSchema})
def create_sale():
    """
    Create a new sales in Database
    Return created sales
    """

    try:
        sale = Sales()

        session = Session()
        session.add(sale) 
        session.commit()

        logger.debug(f"Cannot create a new sale on database!")

        return show_sale(sale), 201
    
    except IntegrityError as e:
        logger.warning(e)

        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Not was possible to save the sale into database"
        logger.warning(e)

        return {"message": error_msg}, 500
