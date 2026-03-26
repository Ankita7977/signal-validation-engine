🚀 Signal Validation & Enforcement Engine (Trust Layer)
📌 Overview

This project implements a strict validation and enforcement layer that ensures only trusted, well-structured signals enter the system.

It acts as a trust boundary between incoming data and the database.

The system guarantees:

No invalid data enters the pipeline
No silent failures occur
Every signal is traceable
Every signal has a confidence score

⚙️ System Flow
data → validation (this layer) → pipeline → database

Validation Rules
1. Dataset ID (NEW)
Must exist
Must not be empty
→ Missing → REJECT

2. Timestamp (UPGRADED)
Must exist
Must follow format: YYYY-MM-DD HH:MM:SS
Must NOT be a future timestamp
→ Invalid → REJECT

3. Coordinates
Latitude must be between -90 and 90
Longitude must be between -180 and 180
→ Invalid → REJECT

4. Feature Type (STRICT)

Allowed values:

movement
communication
environmental

→ Anything else → REJECT

5. Value (UPGRADED)

Accepted:

Integer / Float
Null

Rejected:

Strings (e.g., "abc")
Invalid data types

🧠 Decision Engine Output
Each signal returns:
{
  "status": "ALLOW / REJECT",
  "reason": "Explanation",
  "confidence_score": 0.0 - 1.0
}

📊 Confidence Scoring (NEW)

Confidence is calculated dynamically:

Clean signal → 0.8 – 1.0
Minor issues (e.g., null value) → 0.5 – 0.7
Invalid signal → 0.0

This ensures signals are not just valid, but also trust-rated.

📝 Logging System (UPGRADED)
Rejected signals are stored in:
logs/rejected_signals.log
Each log entry contains:
timestamp | signal_id | dataset_id | reason

🔗 Pipeline Integration 
The validation layer is integrated into a mock pipeline:
for signal:
    result = validate(signal)

    if result["status"] == "ALLOW":
        print("Inserted")
    else:
        print("Rejected")


Test Cases
The system includes edge case testing for:

Missing dataset_id
Future timestamp
Invalid coordinates
Invalid feature type
String value ("45")
Null value

▶️ How to Run
Run test cases:
python tests/test_validator.py

Run demo validation:
python run_demo_validation.py

🎯 Result

This system ensures:

Only validated signals enter the system
Invalid signals are rejected with clear reasons
Every signal has a confidence score
Full traceability is maintained

🚀 Impact

This implementation upgrades the system from:
➡ Basic validation
to
➡ Trust Enforcement Layer with Scoring
