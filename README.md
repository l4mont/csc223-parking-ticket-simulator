# Parking Ticket Simulator

CSC 223 project that simulates a police officer inspecting a parked car and parking meter.

## Project Structure

- `parked_car.py` — validated parked-car data
- `parking_meter.py` — validated purchased parking time
- `parking_ticket.py` — citation data, fine calculation, and ticket report
- `police_officer.py` — inspection and ticket creation
- `main.py` — demonstration program
- `tests/` — automated `unittest` tests
- `Parking_Ticket_Simulator_Report.docx` — project report

## Run the Demonstration

```text
python main.py
```

## Run the Tests

```text
python -m unittest discover -s tests -v
```

The current test suite contains 19 tests covering validation, collaboration, ticket creation, report content, and fine boundaries.

