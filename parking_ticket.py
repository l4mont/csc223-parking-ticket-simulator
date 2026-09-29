"""Define the ParkingTicket class for the parking-ticket simulator."""

from math import ceil


class ParkingTicket:
    """Represent a citation issued for a parking-time violation."""

    def __init__(self, car, officer, illegal_minutes):
        """Create a ticket by copying required car and officer information.

        Args:
            car: ParkedCar-like object with vehicle information.
            officer: PoliceOfficer-like object with officer information.
            illegal_minutes: Positive number of minutes beyond purchased time.
        Raises:
            TypeError: If illegal_minutes is not an integer.
            ValueError: If illegal_minutes is not positive.
        """
        if isinstance(illegal_minutes, bool) or not isinstance(illegal_minutes, int):
            raise TypeError("illegal_minutes must be an integer")
        if illegal_minutes <= 0:
            raise ValueError("illegal_minutes must be positive")
        self._make = car.make
        self._model = car.model
        self._color = car.color
        self._license_number = car.license_number
        self._officer_name = officer.name
        self._badge_number = officer.badge_number
        self._illegal_minutes = illegal_minutes

    @property
    def make(self):
        """Return the cited car's make."""
        return self._make

    @property
    def model(self):
        """Return the cited car's model."""
        return self._model

    @property
    def color(self):
        """Return the cited car's color."""
        return self._color

    @property
    def license_number(self):
        """Return the cited car's license number."""
        return self._license_number

    @property
    def officer_name(self):
        """Return the issuing officer's name."""
        return self._officer_name

    @property
    def badge_number(self):
        """Return the issuing officer's badge number."""
        return self._badge_number

    @property
    def illegal_minutes(self):
        """Return the number of minutes beyond purchased parking time."""
        return self._illegal_minutes

    @property
    def fine(self):
        """Return the fine using the required partial-hour rounding rules."""
        additional_hours = ceil(self.illegal_minutes / 60) - 1
        return 25 + (additional_hours * 10)

    def get_report(self):
        """Return a readable report containing all required ticket information."""
        return (
            "PARKING TICKET\n"
            f"Car: {self.make} {self.model}\n"
            f"Color: {self.color}\n"
            f"License Number: {self.license_number}\n"
            f"Illegal Minutes: {self.illegal_minutes}\n"
            f"Fine: ${self.fine:.2f}\n"
            f"Officer: {self.officer_name}\n"
            f"Badge Number: {self.badge_number}"
        )

    def __str__(self):
        """Return the readable ticket report."""
        return self.get_report()

