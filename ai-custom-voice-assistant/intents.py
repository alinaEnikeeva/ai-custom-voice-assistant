"""
intents.py: Intent detection logic for AI Assistant PoC.
"""

def detect_intent(text: str) -> str | None:
    """
    Rudimentary intent detection based on keywords.
    """
    text_lower = text.lower()
    # New order flow (orthotic flip-flops)
    if any(k in text_lower for k in ["orthotic", "flip-flop", "flip flop"]):
        return "new_order"
    if "order" in text_lower:
        return "order_status"
    if any(k in text_lower for k in ["help", "support", "issue"]):
        return "support"
    return None
