from django.contrib import admin

from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    list_display = (
        "start_location",
        "destination_location",
        "distance_miles",
        "fuel_cost",
        "created_at",
    )