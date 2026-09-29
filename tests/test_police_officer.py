"""Test officer validation and object collaboration."""
import unittest

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class TestPoliceOfficer(unittest.TestCase):
    """Check inspection results and citation snapshots."""

    def test_officer_properties(self):
        """Validate officer identity during construction and assignment."""
        for field in ("name", "badge_number"):
            setattr(self.officer, field, "Updated")
            self.assertEqual(getattr(self.officer, field), "Updated")
            for bad in ("", "   ", None, 123):
                error = ValueError if isinstance(bad, str) else TypeError
                with self.subTest(field=field, value=bad):
                    with self.assertRaises(error):
                        setattr(self.officer, field, bad)
                    values = dict(name="Jordan Lee", badge_number="A-1042")
                    values[field] = bad
                    with self.assertRaises(error):
                        PoliceOfficer(**values)
    def setUp(self):
        """Create fresh objects for each test."""
        self.officer = PoliceOfficer("Jordan Lee", "A-1042")
        self.car = ParkedCar("Toyota", "Camry", "Blue", "ABC-1234", 60)
        self.meter = ParkingMeter(60)

    def test_car_under_purchased_time_returns_none(self):
        """Verify car under purchased time returns none."""
        self.car.minutes_parked = 59
        self.assertIsNone(self.officer.inspect_car(self.car, self.meter))

    def test_car_at_purchased_time_returns_none(self):
        """Verify car at purchased time returns none."""
        self.assertIsNone(self.officer.inspect_car(self.car, self.meter))

    def test_wrong_collaborator_types_raise_type_error(self):
        """Reject invalid dependencies with the required exception type."""
        with self.assertRaises(TypeError):
            self.officer.inspect_car(None, self.meter)
        with self.assertRaises(TypeError):
            self.officer.inspect_car(self.car, None)

    def test_one_minute_over_creates_ticket(self):
        """Verify one minute over creates ticket."""
        self.car.minutes_parked = 61
        ticket = self.officer.inspect_car(self.car, self.meter)
        self.assertIsInstance(ticket, ParkingTicket)
        self.assertEqual(ticket.illegal_minutes, 1)
        self.assertEqual(ticket.fine, 25)

    def test_ticket_contains_collaborating_object_information(self):
        """Verify ticket contains collaborating object information."""
        self.car.minutes_parked = 181
        ticket = self.officer.inspect_car(self.car, self.meter)
        self.assertEqual(ticket.make, self.car.make)
        self.assertEqual(ticket.officer_name, self.officer.name)
        self.assertEqual(ticket.illegal_minutes, 121)
        self.assertEqual(ticket.fine, 45)

    def test_ticket_keeps_copied_values_after_objects_change(self):
        """Verify ticket keeps copied values after objects change."""
        self.car.minutes_parked = 61
        ticket = self.officer.inspect_car(self.car, self.meter)
        self.car.color = "Red"
        self.officer.name = "Changed Name"
        self.assertEqual(ticket.color, "Blue")
        self.assertEqual(ticket.officer_name, "Jordan Lee")


if __name__ == "__main__":
    unittest.main()

