THRESHOLD = 200

class NetworkError(Exception):
    pass

def send_alert_stub(value):
    if value > THRESHOLD:
        raise NetworkError("Alert: Value exceeded threshold!")

def check_value(value):
    try:
        send_alert_stub(value)
    except NetworkError as e:
        return str(e)
    return "All good"

# Production code function using real network sending
def send_alert(value):
    # Imagine this is the real network sending implementation
    pass

def check_value_production(value):
    try:
        send_alert(value)
    except NetworkError as e:
        return str(e)
    return "All good"
