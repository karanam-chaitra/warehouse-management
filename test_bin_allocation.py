import pytest
from bin_allocation import allocate_bin, remove_from_bin_fixed

# --- L4.2 Unit Tests ---
def test_allocate_bin_success():
    bins = {'A1': {'is_free': True, 'class': 'heavy', 'distance': 5}}
    assert allocate_bin('heavy', bins) == 'A1'

def test_allocate_bin_no_free_bins():
    bins = {'A1': {'is_free': False, 'class': 'heavy', 'distance': 5}}
    assert allocate_bin('heavy', bins) is None

def test_allocate_bin_negative_distance_ignored():
    bins = {'A1': {'is_free': True, 'class': 'heavy', 'distance': -5},
            'A2': {'is_free': True, 'class': 'heavy', 'distance': 10}}
    assert allocate_bin('heavy', bins) == 'A2'

def test_allocate_bin_missing_keys_handled_safely():
    bins = {'A1': {'class': 'heavy'}} # Missing is_free and distance
    assert allocate_bin('heavy', bins) is None

# --- L5.4 Code Weakness Tests ---
def test_remove_from_bin_fixed_success():
    assert remove_from_bin_fixed(20, 5) == 15

def test_remove_from_bin_fixed_negative():
    with pytest.raises(ValueError, match="Cannot remove a negative amount"):
        remove_from_bin_fixed(20, -5)

def test_remove_from_bin_fixed_over_removal():
    with pytest.raises(ValueError, match="Cannot remove more stock"):
        remove_from_bin_fixed(10, 15)
