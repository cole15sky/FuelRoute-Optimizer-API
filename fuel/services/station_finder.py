from fuel.services.geocoding_service import GeocodingService
from fuel.models import FuelStation


class StationFinder:

    @staticmethod
    def get_cheapest_stations():

        stations = FuelStation.objects.order_by(
            "retail_price"
        )[:100]

        enriched = []

        for s in stations:
            if s.latitude and s.longitude:
                enriched.append(s)
                continue

            geo = GeocodingService.geocode(
                f"{s.address}, {s.city}, {s.state}"
            )

            if geo:
                s.latitude = geo["lat"]
                s.longitude = geo["lon"]

                enriched.append(s)

        return enriched