import unittest

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class TestPoliceOfficer(unittest.TestCase):
    def setUp(self):
        self.officer = PoliceOfficer("Jordan Lee", "A-1042")
        self.car = ParkedCar("Toyota", "Camry", "Blue", "ABC-1234", 60)
        self.meter = ParkingMeter(60)

    def test_car_under_purchased_time_returns_none(self):
        self.car.minutes_parked = 59
        self.assertIsNone(self.officer.inspect_car(self.car, self.meter))

    def test_car_at_purchased_time_returns_none(self):
        self.assertIsNone(self.officer.inspect_car(self.car, self.meter))

    def test_one_minute_over_creates_ticket(self):
        self.car.minutes_parked = 61
        ticket = self.officer.inspect_car(self.car, self.meter)
        self.assertIsInstance(ticket, ParkingTicket)
        self.assertEqual(ticket.illegal_minutes, 1)
        self.assertEqual(ticket.fine, 25)

    def test_ticket_contains_collaborating_object_information(self):
        self.car.minutes_parked = 181
        ticket = self.officer.inspect_car(self.car, self.meter)
        self.assertEqual(ticket.make, self.car.make)
        self.assertEqual(ticket.officer_name, self.officer.name)
        self.assertEqual(ticket.illegal_minutes, 121)
        self.assertEqual(ticket.fine, 45)

    def test_ticket_keeps_copied_values_after_objects_change(self):
        self.car.minutes_parked = 61
        ticket = self.officer.inspect_car(self.car, self.meter)
        self.car.color = "Red"
        self.officer.name = "Changed Name"
        self.assertEqual(ticket.color, "Blue")
        self.assertEqual(ticket.officer_name, "Jordan Lee")


if __name__ == "__main__":
    unittest.main()

