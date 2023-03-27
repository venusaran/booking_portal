from booking import Booking
import unittest

Booking.instantiate_from_csv()


class TestBookings(unittest.TestCase):
    # need to run these test cases when all the room status is available
    def test_assignment(self):
        self.assertEqual(Booking.assign_room(), "1B", 'The room assignment is wrong.')


if __name__ == '__main__':
    unittest.main()
