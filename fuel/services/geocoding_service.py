import requests


class GeocodingService:

    BASE_URL = (
        "https://nominatim.openstreetmap.org/search"
    )

    @classmethod
    def geocode(cls, location):

        response = requests.get(
            cls.BASE_URL,
            params={
                "q": location,
                "format": "json",
                "limit": 1,
            },
            headers={
                "User-Agent": "FuelRouteOptimizer"
            },
            timeout=20,
        )

        data = response.json()

        if not data:
            return None

        return {
            "lat": float(data[0]["lat"]),
            "lon": float(data[0]["lon"]),
        }