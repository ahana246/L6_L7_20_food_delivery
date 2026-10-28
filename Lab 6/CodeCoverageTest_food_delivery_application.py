import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

#Example test cases:
def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300

# delivery_charge
def test_out_of_range():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)

def test_free_delivery_large_order_in_rain():
    assert delivery_charge(5, 500, True) == 30

def test_medium_distance():
    assert delivery_charge(5, 200, False) == 40

def test_far_distance():
    assert delivery_charge(10, 200, False) == 60

# apply_coupon
def test_invalid_coupon():
    with pytest.raises(ValueError):
        apply_coupon(300, "FAKE", False)

def test_welcome_not_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)

def test_coupon_order_below_minimum():
    assert apply_coupon(150, "SAVE50", False) == 150

def test_coupon_applied():
    assert apply_coupon(300, "SAVE50", False) == 250

# estimated_time
def test_peak_hour_and_busy_restaurant():
    assert estimated_time(5, True, True) == 65
