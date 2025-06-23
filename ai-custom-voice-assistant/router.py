"""
router.py: Routing logic for AI Assistant PoC.
"""

def route_call(intent: str, original_text: str):
    """
    Simulates routing a call based on detected intent.
    """
    routing_map = {
        "order_status": "Orders Team",
        "support": "Support Desk",
    }
    department = routing_map.get(intent)
    if department:
        print(f"Routing to {department} for intent '{intent}'")
    else:
        print(f"[Escalation] No route for intent '{intent}'. Escalating to human agent.")
