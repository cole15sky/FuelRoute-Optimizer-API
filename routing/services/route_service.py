import requests
from django.conf import settings


class RouteService:

    BASE_URL = (
        "https://api.openrouteservice.org/v2/directions/driving-car"
    )

    @classmethod
    def get_route(
        cls,
        start_lon,
        start_lat,
        end_lon,
        end_lat,
    ):
        headers = {
            "Authorization": settings.ORS_API_KEY,
            "Content-Type": "application/json",
        }
        

        payload = {
            "coordinates": [
                [start_lon, start_lat],
                [end_lon, end_lat],
            ]
        }

        response = requests.post(
            cls.BASE_URL,
            json=payload,
            headers=headers,
            timeout=30,
        )



        response.raise_for_status()

        return response.json()

    @staticmethod
    def extract_route(route_response):

        route = route_response["routes"][0]
        summary = route["summary"]

        return {
        "distance_m": summary["distance"],
        "duration_s": summary["duration"],
        "geometry": route["geometry"],
        }