"""Define the ParkingMeter class for the parking-ticket simulator."""


class ParkingMeter:
    """Represent a meter that records purchased parking time."""

    def __init__(self, minutes_purchased):
        """Initialize the meter with validated purchased minutes."""
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        """Return the purchased parking time in minutes."""
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, value):
        """Set purchased minutes; the value must be a nonnegative integer."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("minutes_purchased must be an integer")
        if value < 0:
            raise ValueError("minutes_purchased cannot be negative")
        self._minutes_purchased = value

