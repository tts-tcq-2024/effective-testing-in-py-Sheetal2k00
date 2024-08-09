import unittest
THRESHOLD = 200

class NetworkError(Exception):
    """Custom exception for network-related errors."""
    pass

def check_value(value):
    if value > 250:
        raise NetworkError("Simulated network failure")
    elif value > THRESHOLD:
        return "Alert: Value exceeded threshold!"
    else:
        return "All good"

class TestAlerter(unittest.TestCase):
    def test_value_within_threshold(self):
        self.assertEqual(check_value(150), "All good")
        self.assertEqual(check_value(200), "All good")

    def test_value_exceeds_threshold(self):
        self.assertEqual(check_value(250), "Alert: Value exceeded")

