import pandas as pd

from django.core.management.base import BaseCommand

from fuel.models import FuelStation


class Command(BaseCommand):

    help = "Import fuel stations from CSV"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            default="data/fuel-prices-for-be-assessment.csv"
        )

    def handle(self, *args, **options):

        file_path = options["file"]

        df = pd.read_csv(file_path)

        created_count = 0
        updated_count = 0

        for _, row in df.iterrows():

            station, created = (
                FuelStation.objects.update_or_create(
                    opis_truckstop_id=row["OPIS Truckstop ID"],
                    defaults={
                        "truckstop_name": row["Truckstop Name"],
                        "address": row["Address"],
                        "city": row["City"],
                        "state": row["State"],
                        "rack_id": str(row["Rack ID"]),
                        "retail_price": row["Retail Price"],
                    },
                )
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import completed. "
                f"Created: {created_count}, "
                f"Updated: {updated_count}"
            )
        )