from datetime import datetime
import os

# Allowed feature types
ALLOWED_FEATURE_TYPES = [
    "movement",
    "communication",
    "environmental"
]


def log_rejected_signal(signal, reason):

    # Get project root directory
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )

    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(base_dir, "logs")

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Log file path
    log_file = os.path.join(
        logs_dir,
        "rejected_signals.log"
    )

    # Write log
    with open(log_file, "a") as file:
        file.write(
            f"{datetime.now()} | "
            f"Signal ID: {signal.get('signal_id')} | "
            f"Reason: {reason}\n"
        )


def validate_signal(signal):

    # 1. Check timestamp
    timestamp = signal.get("timestamp")

    if not timestamp:
        log_rejected_signal(signal, "Missing timestamp")
        return {
            "status": "REJECT",
            "reason": "Missing timestamp"
        }

    try:
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        log_rejected_signal(signal, "Invalid timestamp format")
        return {
            "status": "REJECT",
            "reason": "Invalid timestamp format"
        }

    # 2. Check latitude
    latitude = signal.get("latitude")

    if latitude is None:
        log_rejected_signal(signal, "Missing latitude")
        return {
            "status": "REJECT",
            "reason": "Missing latitude"
        }

    if not (-90 <= latitude <= 90):
        log_rejected_signal(signal, "Latitude out of range")
        return {
            "status": "REJECT",
            "reason": "Latitude out of range"
        }

    # 3. Check longitude
    longitude = signal.get("longitude")

    if longitude is None:
        log_rejected_signal(signal, "Missing longitude")
        return {
            "status": "REJECT",
            "reason": "Missing longitude"
        }

    if not (-180 <= longitude <= 180):
        log_rejected_signal(signal, "Longitude out of range")
        return {
            "status": "REJECT",
            "reason": "Longitude out of range"
        }

    # 4. Check feature type
    feature_type = signal.get("feature_type")

    if feature_type not in ALLOWED_FEATURE_TYPES:
        log_rejected_signal(signal, "Invalid feature type")
        return {
            "status": "REJECT",
            "reason": "Invalid feature type"
        }

    # 5. Check value
    value = signal.get("value")

    if value is not None and not isinstance(value, (int, float)):
        log_rejected_signal(signal, "Value must be number or null")
        return {
            "status": "REJECT",
            "reason": "Value must be number or null"
        }

    # If everything is valid
    return {
        "status": "ALLOW",
        "reason": "Valid signal"
    }
    