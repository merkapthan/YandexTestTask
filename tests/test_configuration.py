# This test checks very simple function, but we imagine a situation (wrote about it in configuration.py) when we use
# more complicated way to co get config, which turns into dictionary as a result

from delivery_function.configuration import get_config


expected_config = {
    "base_cost": 400.0,
    "fragile_factors": {
        "is_fragile": 300.0,
        "allowed_km": 30.0
    },
    "distance_factors": {
        "closer_than_2": 50.0,
        "closer_than_10": 100.0,
        "closer_than_30": 200.0,
        "more_than_30": 300.0
    },
    "size_factors": {
        "small": 100.0,
        "large": 200.0
    },
    "load_level_multipliers": {
        "base": 1.0,
        "increased": 1.2,
        "high": 1.4,
        "extreme": 1.6
    }
}


def test_get_config():
    config = get_config()
    assert config == expected_config, f'Expected {expected_config}, but got {config}'