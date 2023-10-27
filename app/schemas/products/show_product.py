from app.models.product import Product

def show_product (product: Product):
    """
    Return an representation of One Product.
    """
    return {
        "id": product.id,
        "name": product.name,
        "value": product.value,
        "created_at": product.created_at,
        "updated_at": product.updated_at
    }