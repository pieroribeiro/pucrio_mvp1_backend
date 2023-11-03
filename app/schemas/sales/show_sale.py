from app.models.sales import Sales

def show_sale (sale: Sales):
    """
    Return an representation of One Sale.
    """
    return {
        "id": sale.id,
        "created_at": sale.created_at
    }