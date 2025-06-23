"""
ringcx.py: Stub for RingCX API integration.
"""

def receive_call():
    """
    Simulates receiving an inbound call. Returns a call ID and dummy audio data.
    """
    call_id = "CALL12345"
    audio_data = "<audio_stream>"
    print(f"[RingCX] Received call with ID: {call_id}")
    return call_id, audio_data
