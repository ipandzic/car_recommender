from django.core.management.base import BaseCommand
import pandas as pd
from recommender.models import Vehicle
from django.utils.dateparse import parse_datetime


class Command(BaseCommand):
    help = 'Load data from an Excel file into the Vehicle model.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file.')

    def handle(self, *args, **options):
        file_path = options['file_path']
        data = pd.read_excel(file_path, engine='openpyxl')

        vehicles = []
        count = 0
        for _, row in data.iterrows():
            count += 1
            if count > 3:
                Vehicle.objects.bulk_create(vehicles)
                return
            print(row['Make'])
            print("*******", count)
            vehicle = Vehicle(
                make=row['Make'],
                model=row['Model'],
                year=row.get('Year', None),
                created_on=parse_datetime(row['Created On']).date() if pd.notna(row['Created On']) else None,
                modified_on=parse_datetime(row['Modified On']).date() if pd.notna(row['Modified On']) else None,
                start_stop=row['Start-Stop'] == 'Y',
                #Map other fields accordingly
            )
            vehicles.append(vehicle)

        Vehicle.objects.bulk_create(vehicles)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(vehicles)} vehicles.'))