from django.db import models


class Trip(models.Model):

    start_location = models.CharField(
        max_length=255
    )

    destination_location = models.CharField(
        max_length=255
    )

    distance_miles = models.FloatField(
        null=True,
        blank=True
    )

    duration_minutes = models.FloatField(
        null=True,
        blank=True
    )

    fuel_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.start_location} → "
            f"{self.destination_location}"
        )