from delivery_function.function import Delivery
import pytest

@pytest.fixture(scope='module')
def calculator():
    return Delivery()

@pytest.mark.parametrize(
    "distance, is_fragile, load_level, size, expected_result",
    [
        (40, False, 'base', 'large', 900.0),
        (40, False, 'increased', 'large', 1080.0),
        (40, False, 'high', 'large', 1260.0),
        (40, False, 'extreme', 'large', 1440.0),
        (40, False, 'extreme', 'small', 1280.0),
        (1, False, 'extreme', 'small', 880.0),
        (5, False, 'extreme', 'small', 960.0),
        (20, False, 'extreme', 'small', 1120.0),
        (20, True, 'extreme', 'small', 1600.0),
        (40, True, 'extreme', 'small', 'Fragile goods can not be transported over a distance of more than 30.0 km'),
    ]
)
def test_delivery_function_correct(calculator, distance, is_fragile, load_level, size, expected_result):
    result = calculator.calculate_delivery_cost(distance, is_fragile, load_level, size)
    assert result == expected_result, f'{result = }, but {expected_result} expected'

#We definitely can parametrize next two tests, but it will take more lines, then two separate tests
def test_delivery_function_wrong_load_level(calculator):
    with pytest.raises(ValueError,
                       match='Invalid load level invalid_load_level, valid levels are base, increased, high, extreme'):
        calculator.calculate_delivery_cost(40, False, 'invalid_load_level', 'large')

def test_delivery_function_wrong_size(calculator):
    with pytest.raises(ValueError, match='Invalid size invalid_size, valid sizes are small, large'):
        calculator.calculate_delivery_cost(40, False, 'base', 'invalid_size')

