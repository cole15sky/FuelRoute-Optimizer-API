from math import dist


class FuelOptimizer:

    MAX_RANGE = 500  # miles
    MPG = 10

    def __init__(self, route_points, stations):
        self.route_points = route_points
        self.stations = stations

    def distance(self, a, b):
        # rough conversion lat/lon → miles
        return dist(a, b) * 69

    def find_stations_near_point(self, point, radius=50):
        nearby = []

        for station in self.stations:
            s_point = (
                station.latitude,
                station.longitude
            )

            if self.distance(point, s_point) <= radius:
                nearby.append(station)

        return nearby

    def choose_cheapest(self, stations):
        if not stations:
            return None

        return min(
            stations,
            key=lambda x: x.retail_price
        )

    def generate_fuel_stops(self):
        stops = []
        traveled = 0

        for i in range(1, len(self.route_points)):
            segment = self.distance(
                self.route_points[i - 1],
                self.route_points[i]
            )

            traveled += segment

            if traveled >= self.MAX_RANGE:
                candidates = self.find_stations_near_point(
                    self.route_points[i]
                )

                best = self.choose_cheapest(candidates)

                if best:
                    stops.append({
                        "name": best.name,
                        "price": best.retail_price,
                        "lat": best.latitude,
                        "lon": best.longitude,
                    })

                traveled = 0

        return stops