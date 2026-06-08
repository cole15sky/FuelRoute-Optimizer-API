from fuel.services.geocoding_service import GeocodingService
from routing.services.route_service import RouteService
from fuel.services.station_finder import StationFinder
from fuel.services.fuel_optimizer import FuelOptimizer


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

        # FUEL LOGIC 

        # simple route points for fuel stop generation
        route_points = [
            (start["lat"], start["lon"]),
            (destination["lat"], destination["lon"])
        ]

        stations = StationFinder.get_cheapest_stations()
        optimizer = FuelOptimizer(route_points, stations)
        fuel_stops = optimizer.generate_fuel_stops()

        MPG = 10

        gallons = distance_miles / MPG

        avg_price = (
            sum(s["price"] for s in fuel_stops) / len(fuel_stops)
            if fuel_stops else 0
        )

        total_cost = gallons * avg_price if avg_price else 0

        return {
            "start": start_location,
            "destination": destination_location,
            "distance_miles": round(distance_miles, 2),
            "duration_hours": round(duration_hours, 2),

            # REQUIRED OUTPUTS
            "fuel_stops": fuel_stops,
            "total_fuel_cost": round(total_cost, 2),
        }