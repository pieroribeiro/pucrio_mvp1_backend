from sqlalchemy.exc import IntegrityError

from app.helpers.logger import logger
from app.schemas.sales_items.create_sale_item_schema import CreateSaleItemSchema
from app.schemas.sales_items.view_sales_items_schema import ViewSalesItemsSchema
from app.schemas.sales_items.show_sale_item import show_sale_item

from app.schemas.errors.generic_error_schema import GenericErrorSchema
from app.models import Session, Sales, Products, Sales_Items
from app.openapi_tags.sales_items import Tag_Sales_Items
from app import app

# Route: Create Product
@app.post("/sales_items/<int:sale_id>/<int:product_id>/<string:product_quantity>", tags = [Tag_Sales_Items], responses={"201": ViewSalesItemsSchema, "500": GenericErrorSchema})
def create_sales_items(path: CreateSaleItemSchema):
    """
    Create a new sale items in Database
    Return created sale items
    """

    product_quantity    = path.product_quantity

    try:
        product_quantity = float(product_quantity)
    except Exception as e:
        logger.warning(e)
        return {"message": "Not was possible to convert quantity of product to Float"}, 500


    try:        

        sale_id             = path.sale_id
        product_id          = path.product_id

        session = Session()
        sale = session.query(Sales).filter(Sales.id == sale_id).first()

        ## DELETE ALL SALES ITEMS - for tests only
        # deleteSalesItems = session.query(Sales_Items).delete()
        # session.commit()

        # Verify if Sale exists
        if sale: 
            # insert product in sales_items
            sale_item = Sales_Items(sale_id = sale_id, product_id = product_id, product_quantity = product_quantity)
            session.add(sale_item)
            session.commit()
            
            total_sale = 0

            # get all products from sale
            products_of_sale = get_products_of_sale(session, sale_id)
            
            # calculate products value
            if products_of_sale:
                for product_in_sale in products_of_sale:
                    prod_sale_qtd = product_in_sale.product_quantity
                    prod_sale_id = product_in_sale.product_id
                    
                    product_info = get_product_info(session, prod_sale_id)

                    total_sale = float(product_info.value) * float(prod_sale_qtd)

                logger.warning(f"total_sale: {total_sale}")

                # update total of sale
                sale.total = total_sale
                session.commit()

            logger.debug(f"The item '{product_id}' of Sale '{sale_id}' has been saved on database!")

            return show_sale_item(sale_item), 201
        else:
            return {"message": "Sale not found on database"}, 404
    
    except IntegrityError as e:
        logger.warning(e)

        return {"message": f"This product '{product_id}' already exists in this sale '{sale_id}'."}, 500

    except Exception as e:
        logger.warning(e)

        return {"message": "Not was possible to save the item of sale into database."}, 500

def get_products_of_sale (session, sale_id: int):
    return session.query(Sales_Items).filter(Sales_Items.sale_id == sale_id)

def get_product_info (session, product_id: int):
    return session.query(Products).filter(Products.id == product_id).first()