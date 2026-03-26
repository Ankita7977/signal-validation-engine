from src.validation.signal_validator import validate_signal

signals = [
    {
        "signal_id": 1,
        "dataset_id": 1,
        "timestamp": "2025-03-25 10:30:00",
        "latitude": 28.6,
        "longitude": 77.2,
        "feature_type": "movement",
        "value": 45
    }, 
    {
        "signal_id": 2,
        "timestamp": "2025-03-25 10:30:00"
    }
]

for s in signals:
    result = validate_signal(s)
    print(result)
