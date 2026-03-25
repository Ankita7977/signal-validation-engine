import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.validation.signal_validator import validate_signal


# Test signals
signals = [

    {
        "signal_id": 1,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": 45
    },

    {
        "signal_id": 2,
        "timestamp": "",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": 45
    },

    {
        "signal_id": 3,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 200,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": 45
    },

    {
        "signal_id": 4,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "invalid",
        "value": "abc"
    }

]


# Run validation
for signal in signals:

    result = validate_signal(signal)

    print(
        f"Signal {signal['signal_id']} -> "
        f"{result['status']} : "
        f"{result['reason']}"
    )