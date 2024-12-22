import pprint
delivery_config = {
    "delivery": {
        "baze_cost": 400.0,
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
            "baze": 1.0,
            "increased": 1.2,
            "high": 1.4,
            "extreme": 1.6
        }
    }
}
if __name__ == '__main__':
    pprint.pprint(delivery_config)


