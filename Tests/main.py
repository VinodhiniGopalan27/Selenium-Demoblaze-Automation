import unittest
from tests.test_placeorder import TestPlaceOrder
from tests.test_cart import TestCart
from tests.test_login import TestLogin
from tests.test_signup import TestSignup

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSignup))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCart))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPlaceOrder))
    runner = unittest.TextTestRunner()
    runner.run(suite)
