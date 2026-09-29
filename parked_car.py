"""Define the ParkedCar class for the parking-ticket simulator."""


class ParkedCar:
    """Represent a car parked at a metered space."""

    def __init__(self, make, model, color, license_number, minutes_parked):
        """Initialize a car and validate all supplied values."""
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @staticmethod
    def _validate_text(value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty")
        return value

    @property
    def make(self):
        """Return the car's make."""
        return self._make

    @make.setter
    def make(self, value):
        """Set the car's make, rejecting empty or non-string values."""
        self._make = self._validate_text(value, "make")

    @property
    def model(self):
        """Return the car's model."""
        return self._model

    @model.setter
    def model(self, value):
        """Set the car's model, rejecting empty or non-string values."""
        self._model = self._validate_text(value, "model")

    @property
    def color(self):
        """Return the car's color."""
        return self._color

    @color.setter
    def color(self, value):
        """Set the car's color, rejecting empty or non-string values."""
        self._color = self._validate_text(value, "color")

    @property
    def license_number(self):
        """Return the car's license number."""
        return self._license_number

    @license_number.setter
    def license_number(self, value):
        """Set the license number, rejecting empty or non-string values."""
        self._license_number = self._validate_text(value, "license_number")

    @property
    def minutes_parked(self):
        """Return the number of minutes the car has been parked."""
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, value):
        """Set parked minutes; the value must be a nonnegative integer."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("minutes_parked must be an integer")
        if value < 0:
            raise ValueError("minutes_parked cannot be negative")
        self._minutes_parked = value

