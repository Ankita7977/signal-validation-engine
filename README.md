# Signal Validation & Enforcement Engine

## Overview

This project implements a validation layer that checks incoming signal data before it enters the system database.

The validator ensures that only correct data is accepted and incorrect data is rejected and logged.

---

## Validation Rules

The system checks the following:

1. Timestamp
   - Must exist
   - Must be in format YYYY-MM-DD HH:MM:SS

2. Coordinates
   - Latitude must be between -90 and 90
   - Longitude must be between -180 and 180

3. Feature Type
   Allowed values:
   - movement
   - communication
   - environmental

4. Value
   - Must be a number or null

---

## Decision Output

The validator returns:

ALLOW — if data is valid  
REJECT — if data is invalid  

Each rejection includes a reason.

---

## Logging

Rejected signals are recorded in:

logs/rejected_signals.log

Each log entry includes:

- signal_id
- reason
- timestamp

---

## How to Run

Run the test file:

python tests/test_validator.py

---

## Result

The system prevents incorrect data from entering the pipeline and ensures data integrity.