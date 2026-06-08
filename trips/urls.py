from django.urls import path
from .views import TripOptimizeView


urlpatterns = [
    path(
        "trips/optimize/",
        TripOptimizeView.as_view(),
        name="trip-optimize"
    ),
]