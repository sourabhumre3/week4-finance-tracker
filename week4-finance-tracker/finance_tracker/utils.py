def validate_amount(value):
    try:
        return float(value)
    except:
        return None