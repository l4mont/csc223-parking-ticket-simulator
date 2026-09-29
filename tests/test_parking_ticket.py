"""Test citation details, fine boundaries, and readable reports."""
import io
import unittest
from contextlib import redirect_stdout

from parked_car import ParkedCar
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class TestParkingTicket(unittest.TestCase):
    """Check ticket data and fine rules."""

    def test_all_invalid_illegal_minutes(self):
        """Reject nonpositive minutes and incorrect types."""
        for bad in (0, -1, True, None, "1", 1.5):
            error = ValueError if type(bad) is int else TypeError
            with self.subTest(value=bad), self.assertRaises(error):
                ParkingTicket(self.car, self.officer, bad)

    def test_all_copied_fields(self):
        """Verify all vehicle fields are copied into the citation."""
        ticket = ParkingTicket(self.car, self.officer, 1)
        for field in ("make", "model", "color", "license_number"):
            self.assertEqual(getattr(ticket, field), getattr(self.car, field))
    def setUp(self):
        """Create fresh objects for each test."""
        self.car = ParkedCar("Toyota", "Camry", "Blue", "ABC-1234", 61)
        self.officer = PoliceOfficer("Jordan Lee", "A-1042")

    def test_copies_car_and_officer_information(self):
        """Verify copies car and officer information."""
        ticket = ParkingTicket(self.car, self.officer, 1)
        self.assertEqual(ticket.make, "Toyota")
        self.assertEqual(ticket.license_number, "ABC-1234")
        self.assertEqual(ticket.officer_name, "Jordan Lee")
        self.assertEqual(ticket.badge_number, "A-1042")
        self.assertEqual(ticket.illegal_minutes, 1)

    def test_fine_boundaries(self):
        """Verify fine boundaries."""
        expected = {1: 25, 60: 25, 61: 35, 120: 35, 121: 45}
        for minutes, fine in expected.items():
            with self.subTest(minutes=minutes):
                self.assertEqual(ParkingTicket(self.car, self.officer, minutes).fine, fine)

    def test_invalid_illegal_minutes_are_rejected(self):
        """Verify invalid illegal minutes are rejected."""
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, 0)
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, 1.5)

    def test_report_contains_required_information(self):
        """Verify report contains required information."""
        ticket = ParkingTicket(self.car, self.officer, 61)
        output = io.StringIO()
        with redirect_stdout(output):
            print(ticket.get_report())
        report = output.getvalue()
        for value in ("Toyota", "Camry", "Blue", "ABC-1234", "61", "$35.00", "Jordan Lee", "A-1042"):
            self.assertIn(value, report)


if __name__ == "__main__":
    unittest.main()

