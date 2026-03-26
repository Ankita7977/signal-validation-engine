import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.validation.signal_validator import validate_signal


signals = [

    # ✅ Valid
    {
        "signal_id": 1,
        "dataset_id": 1,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": 45
    },

    # ❌ Missing dataset_id
    {
        "signal_id": 2,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": 45
    },

    # ❌ Future timestamp
    {
        "signal_id": 3,
        "dataset_id": 1,
        "timestamp": "2035-03-25 10:30:00",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": 45
    },

    # ❌ Invalid latitude
    {
        "signal_id": 4,
        "dataset_id": 1,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 200,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": 45
    },

    # ❌ String value
    {
        "signal_id": 5,
        "dataset_id": 1,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": "45"
    },

    # ⚠️ Null value (allowed but lower confidence)
    {
        "signal_id": 6,
        "dataset_id": 1,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": None
    }
]


for signal in signals:

    result = validate_signal(signal)

    print(
        f"Signal {signal['signal_id']} -> "
        f"{result['status']} | "
        f"{result['reason']} | "
        f"Confidence: {result['confidence_score']}"
    )
