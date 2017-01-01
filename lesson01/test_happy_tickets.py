import unittest
from happy_tickets import count_happy_tickets

class TestHappyTickets(unittest.TestCase):
    def test_happy_tickets(self):
        self.assertEqual(count_happy_tickets(0, 0), 1)
        self.assertEqual(count_happy_tickets(1, 1), 0)
        self.assertEqual(count_happy_tickets(1, 1000), 0)
        self.assertEqual(count_happy_tickets(0, 1001), 2)
        self.assertEqual(count_happy_tickets(0, 999999), 55251)
        self.assertEqual(count_happy_tickets(1, 999999), 55252)

if __name__ == "__main__":
    unittest.main()
