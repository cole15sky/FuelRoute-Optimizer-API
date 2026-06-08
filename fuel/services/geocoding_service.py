import requests


class GeocodingService:

    BASE_URL = "https://nominatim.openstreetmap.org/search"
    backup_url = "https://api.opencagedata.com/geocode/v1/json"

    @classmethod
    def geocode(cls, location):

        try:
            response = requests.get(
                cls.BASE_URL,
                params={
                    "q": location,
                    "format": "json",
                    "limit": 1,
                },
                headers={
                    # 🔥 REQUIRED: real identity
                    "User-Agent": "FuelRouteOptimizer/1.0 (student project - contact: your_email@example.com)",
                    "Accept-Language": "en",
                },
                timeout=20,
            )

            response.raise_for_status()

            data = response.json()

            if not data:
                return None

            return {
                "lat": float(data[0]["lat"]),
                "lon": float(data[0]["lon"]),
            }

        except requests.exceptions.HTTPError as e:
            print("Geocoding HTTP error:", e)
            return None

        except Exception as e:
            print("Geocoding error:", e)
            return None