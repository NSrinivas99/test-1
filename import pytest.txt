import pytest
import numpy as np
from your_project import Tomato  # replace with the actual module and class names

# Sample tomato data
sample_tomatoes = [
    {"type": "Roma", "weight_g": 150, "price_per_kg": 2.5, "color": "Red", "ripeness": "Ripe"},
    {"type": "Cherry", "weight_g": 20, "price_per_kg": 3.0, "color": "Red", "ripeness": "Ripe"},
    {"type": "Heirloom", "weight_g": 200, "price_per_kg": 4.5, "color": "Yellow", "ripeness": "Unripe"}
]

# Test if tomato price calculation works correctly
def test_calculate_price():
    tomato = Tomato(type="Roma", weight_g=150, price_per_kg=2.5)
    expected_price = (150 / 1000) * 2.5
    assert tomato.calculate_price() == expected_price

# Test if the average weight calculation works for multiple tomatoes
def test_average_weight():
    weights = [tomato["weight_g"] for tomato in sample_tomatoes]
    average_weight = np.mean(weights)
    assert np.isclose(average_weight, 123.33, atol=0.1)  # adjust tolerance as needed

# Test if the ripeness assessment works correctly
@pytest.mark.parametrize("ripeness, expected_result", [
    ("Ripe", True),
    ("Unripe", False),
    ("Overripe", False)
])
def test_is_ripe(ripeness, expected_result):
    tomato = Tomato(type="Cherry", weight_g=20, price_per_kg=3.0, ripeness=ripeness)
    assert tomato.is_ripe() == expected_result

# Test if color-based grouping works (if such a function exists)
def test_group_by_color():
    grouped = Tomato.group_by_color(sample_tomatoes)
    assert "Red" in grouped
    assert "Yellow" in grouped
    assert len(grouped["Red"]) == 2
    assert len(grouped["Yellow"]) == 1

# Example of testing an error or exception
def test_invalid_weight():
    with pytest.raises(ValueError):
        Tomato(type="Roma", weight_g=-50, price_per_kg=2.5)  # Negative weight should raise an error
