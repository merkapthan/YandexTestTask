from configuration import get_config

class Delivery:
    def __init__(self):
        self._config = get_config()

    def calculate_delivery_cost(self, distance: float, is_fragile: bool, load_level: str, size: str):
        valid_load_levels = list(self._config["load_level_multipliers"]) #['base', 'increased', 'high', 'extreme']
        valid_sizes = list(self._config["size_factors"])                 #['small', 'large']

        if load_level not in valid_load_levels:
            raise ValueError(f'Invalid load level {load_level}, valid levels are {", ".join(valid_load_levels)}')
        if size not in valid_sizes:
            raise ValueError(f'Invalid size {size}, valid sizes are {", ".join(valid_sizes)}')

        result = self._config['base_cost']
        if is_fragile:
            if distance > 30:
                # Not realised like error, it is a part of planned scenario
                return (f"Fragile goods can not be transported over a distance of more "
                       f"than {self._config['fragile_factors']['allowed_km']} km")
            result += self._config['fragile_factors']['is_fragile']

        result += (
            self._config["distance_factors"]["more_than_30"] if distance > 30 else
            self._config["distance_factors"]["closer_than_30"] if distance > 10 else
            self._config["distance_factors"]["closer_than_10"] if distance > 2 else
            self._config["distance_factors"]["closer_than_2"]
        )
        result += self._config["size_factors"][size]
        result *= self._config["load_level_multipliers"][load_level]

        return result
