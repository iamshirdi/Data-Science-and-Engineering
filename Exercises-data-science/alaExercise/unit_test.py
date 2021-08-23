
import unittest
class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test_B(self):
        from ala_test import routing_price
        self.assertEqual(routing_price(4673212345),1)

    def test_A(self):
        from ala_test import routing_price
        self.assertEqual(routing_price(4620212345),2)

    def test_A2(self):
        from ala_test import routing_price
        self.assertEqual(routing_price(1462021234),2)

    def test_W(self): #Wrong
        from ala_test import routing_price
        self.assertEqual(routing_price(9473212345),4)

    # def test_E(self): #Equal for more routes
    #     from ala_test import routing_price
    #     self.assertEqual(routing_price(4673212345),3)

if __name__ == '__main__':
    unittest.main()
