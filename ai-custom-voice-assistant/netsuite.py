"""
netsuite.py: Stub for NetSuite ERP integration.
"""

def get_customer_order(query: str) -> dict:
    """
    Simulates fetching order information from NetSuite.
    """
    # In a real system, use NetSuite API client
    print(f"[NetSuite] Looking up order for query: '{query}'")
    # Return dummy order info
    return {"order_id": "ORD123", "status": "Shipped", "eta": "2025-06-25"}
