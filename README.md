# Parking Ticket Simulator

CSC 223 project that simulates a police officer inspecting a parked car and parking meter.

## Project Structure

- `parked_car.py` — validated parked-car data
- `parking_meter.py` — validated purchased parking time
- `parking_ticket.py` — citation data, fine calculation, and ticket report
- `police_officer.py` — inspection and ticket creation
- `main.py` — demonstration program
- `tests/` — automated `unittest` tests

## Run the Demonstration

```text
python main.py
```

## Run the Tests

```text
python -m unittest discover -s tests -v
```

The current test suite contains 26 tests covering validation, collaboration, ticket creation, report content, and fine boundaries. Tested with Python 3.12.14. No third-party packages are needed.

Student: Emory Bruington. IDE: Visual Studio. Open the folder as a Python project, select a Python interpreter, and set `main.py` as the startup file. Run the test command above from the project root.

The current report is included as [Parking_Ticket_Simulator_Report.pdf](Parking_Ticket_Simulator_Report.pdf). Submit this same PDF separately with the repository URL.

