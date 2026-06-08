class FuelOptimizer:

    MPG = 10

    MAX_RANGE = 500

    TANK_CAPACITY = 50

    @classmethod
    def gallons_needed(
        cls,
        distance_miles,
    ):
        return distance_miles / cls.MPG