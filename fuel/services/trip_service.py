from fuel.services.geocoding_service import GeocodingService
from routing.services.route_service import RouteService


class TripService:

    @classmethod
    def optimize_trip(
        cls,
        start_location,
        destination_location,
    ):
        start = GeocodingService.geocode(
            start_location
        )

        if not start:
            raise ValueError(
                "Invalid start location"
            )

        destination = GeocodingService.geocode(
            destination_location
        )

        if not destination:
            raise ValueError(
                "Invalid destination location"
            )

        route_response = RouteService.get_route(
            start["lon"],
            start["lat"],
            destination["lon"],
            destination["lat"],
        )

        route_data = RouteService.extract_route(
            route_response
        )

        distance_miles = (
            route_data["distance_m"] / 1609.34
        )

        duration_hours = (
            route_data["duration_s"] / 3600
        )

        return {
            "start": start_location,
            "destination": destination_location,
            "distance_miles": round(
                distance_miles,
                2,
            ),
            "duration_hours": round(
                duration_hours,
                2,
            ),
        }