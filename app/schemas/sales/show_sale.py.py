from app.models.sales import Sales

def show_sale (sale: Sales):
    """
    Return an representation of One Sale.
    """
    return {
        "id": sales.id,
        "created_at": sales.created_at
    }