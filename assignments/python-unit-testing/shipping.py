def calculate_shipping(weight_kg):
    if weight_kg <= 0:
        raise ValueError("Weight must be positive")
    return 5 + 2 * weight_kg