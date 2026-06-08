from fuel.models import FuelStation


class StationFinder:

    @staticmethod
    def get_cheapest_stations():

        return FuelStation.objects.order_by(
            "retail_price"
        )[:100]