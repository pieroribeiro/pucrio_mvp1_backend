from app.models.tables import Products

def show_product (product: Products):
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