import requests


class GeocodingService:

    BASE_URL = "https://nominatim.openstreetmap.org/search"

    @classmethod
    def geocode(cls, location):

        if not location:
            return None

        try:
            response = requests.get(
                cls.BASE_URL,
                params={
                    "q": location,
                    "format": "json",
                    "limit": 1
                },
                headers={
                    "User-Agent": "FuelRouteOptimizer/1.0"
                },
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            if not data:
                return None

            return {
                "lat": float(data[0]["lat"]),
                "lon": float(data[0]["lon"]),
            }

        except (requests.exceptions.RequestException, ValueError):
            return None