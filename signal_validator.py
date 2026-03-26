from datetime import datetime
import os

# Allowed feature types
ALLOWED_FEATURE_TYPES = [
    "movement",
    "communication",
    "environmental"
]

 
# ---------------- LOGGING ----------------
def log_rejected_signal(signal, reason):

    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )

    logs_dir = os.path.join(base_dir, "logs")

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    log_file = os.path.join(logs_dir, "rejected_signals.log")

    with open(log_file, "a") as file:
        file.write(
            f"{datetime.now()} | "
            f"{signal.get('signal_id')} | "
            f"{signal.get('dataset_id')} | "
            f"{reason}\n"
        )


# ---------------- CONFIDENCE ----------------
def calculate_confidence(signal):

    score = 1.0

    # Reduce score if value is null
    if signal.get("value") is None:
        score -= 0.3

    # Reduce score if dataset_id missing
    if not signal.get("dataset_id"):
        score -= 0.5

    return max(0.0, min(score, 1.0))


# ---------------- VALIDATION ----------------
def validate_signal(signal):

    # 1. Dataset ID (NEW)
    dataset_id = signal.get("dataset_id")

    if not dataset_id:
        log_rejected_signal(signal, "Missing dataset_id")
        return {
            "status": "REJECT",
            "reason": "Missing dataset_id",
            "confidence_score": 0.0
        }

    # 2. Timestamp (UPGRADE)
    timestamp = signal.get("timestamp")

    if not timestamp:
        log_rejected_signal(signal, "Missing timestamp")
        return {
            "status": "REJECT",
            "reason": "Missing timestamp",
            "confidence_score": 0.0
        }

    try:
        ts = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        if ts > datetime.now():
            log_rejected_signal(signal, "Future timestamp not allowed")
            return {
                "status": "REJECT",
                "reason": "Future timestamp not allowed",
                "confidence_score": 0.0
            }

    except ValueError:
        log_rejected_signal(signal, "Invalid timestamp format")
        return {
            "status": "REJECT",
            "reason": "Invalid timestamp format",
            "confidence_score": 0.0
        }

    # 3. Latitude
    latitude = signal.get("latitude")

    if latitude is None:
        log_rejected_signal(signal, "Missing latitude")
        return {
            "status": "REJECT",
            "reason": "Missing latitude",
            "confidence_score": 0.0
        }

    if not (-90 <= latitude <= 90):
        log_rejected_signal(signal, "Latitude out of range")
        return {
            "status": "REJECT",
            "reason": "Latitude out of range",
            "confidence_score": 0.0
        }

    # 4. Longitude
    longitude = signal.get("longitude")

    if longitude is None:
        log_rejected_signal(signal, "Missing longitude")
        return {
            "status": "REJECT",
            "reason": "Missing longitude",
            "confidence_score": 0.0
        }

    if not (-180 <= longitude <= 180):
        log_rejected_signal(signal, "Longitude out of range")
        return {
            "status": "REJECT",
            "reason": "Longitude out of range",
            "confidence_score": 0.0
        }

    # 5. Feature Type
    feature_type = signal.get("feature_type")

    if feature_type not in ALLOWED_FEATURE_TYPES:
        log_rejected_signal(signal, "Invalid feature type")
        return {
            "status": "REJECT",
            "reason": "Invalid feature type",
            "confidence_score": 0.0
        }

    # 6. Value
    value = signal.get("value")

    if value is not None and not isinstance(value, (int, float)):
        log_rejected_signal(signal, "Value must be number or null")
        return {
            "status": "REJECT",
            "reason": "Value must be number or null",
            "confidence_score": 0.0
        }

    # FINAL RESULT
    confidence = calculate_confidence(signal)

    return {
        "status": "ALLOW",
        "reason": "Valid signal",
        "confidence_score": confidence
    }
