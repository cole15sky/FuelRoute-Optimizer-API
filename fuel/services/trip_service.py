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
        # GEOCODING
        start = GeocodingService.geocode(start_location)

        if not start:
            raise ValueError("Invalid start location")

        destination = GeocodingService.geocode(destination_location)

        if not destination:
            raise ValueError("Invalid destination location")

        # ROUTE FETCH
        route_response = RouteService.get_route(
            start["lon"],
            start["lat"],
            destination["lon"],
            destination["lat"],
        )

        route_data = RouteService.extract_route(route_response)

        distance_miles = route_data["distance_m"] / 1609.34
        duration_hours = route_data["duration_s"] / 3600

        # ROUTE POINTS (for fuel logic)
        route_points = [
            (start["lat"], start["lon"]),
            (destination["lat"], destination["lon"]),
        ]

        # FUEL OPTIMIZATION
        stations = StationFinder.get_cheapest_stations()
        optimizer = FuelOptimizer(route_points, stations)
        fuel_stops = optimizer.generate_fuel_stops()

        # COST CALCULATION
        MPG = 10
        gallons = distance_miles / MPG

        if fuel_stops:
            avg_price = sum(
                s["price"] for s in fuel_stops
            ) / len(fuel_stops)
        else:
            avg_price = 0

        total_cost = gallons * avg_price if avg_price else 0

        # FINAL RESPONSE
        return {
            "start": start_location,
            "destination": destination_location,
            "distance_miles": round(distance_miles, 2),
            "duration_hours": round(duration_hours, 2),

            "fuel_stops": fuel_stops,
            "total_fuel_cost": round(total_cost, 2),
        }