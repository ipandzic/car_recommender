from django.core.management.base import BaseCommand
import pandas as pd
from recommender.models import Vehicle
from django.utils.dateparse import parse_datetime


def preprocess_range(value):
    if pd.notna(value) and '/' in str(value):
        numbers = value.split('/')
        # Convert strings to floats and calculate the average
        if len(numbers) == 2:
            try:
                average = sum(float(num) for num in numbers) / len(numbers)
                return average
            except ValueError:
                return None
    return value


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
            # count += 1
            # if count > 3:
            #     Vehicle.objects.bulk_create(vehicles)
            #     return
            # print(row['Make'])
            # print("*******", count)
            vehicle = Vehicle(
                make=row['Make'],
                model=row['Model'],
                annual_petroleum_consumption_for_fuel_type1=row['Annual Petroleum Consumption For Fuel Type1'],
                annual_petroleum_consumption_for_fuel_type2=row['Annual Petroleum Consumption For Fuel Type2'],
                time_to_charge_at_120v=row['Time to charge at 120V'],
                time_to_charge_at_240v=row['Time to charge at 240V'],
                city_mpg_for_fuel_type1=row['City Mpg For Fuel Type1'],
                unrounded_city_mpg_for_fuel_type1=row['Unrounded City Mpg For Fuel Type1 (2)'],
                city_mpg_for_fuel_type2=row['City Mpg For Fuel Type2'],
                unrounded_city_mpg_for_fuel_type2=row['Unrounded City Mpg For Fuel Type2'],
                city_gasoline_consumption=row['City gasoline consumption'],
                city_electricity_consumption=row['City electricity consumption'],
                epa_city_utility_factor=row['EPA city utility factor'],
                co2_fuel_type1=row['Co2 Fuel Type1'],
                co2_fuel_type2=row['Co2 Fuel Type2'],
                co2_tailpipe_for_fuel_type2=row['Co2  Tailpipe For Fuel Type2'],
                co2_tailpipe_for_fuel_type1=row['Co2  Tailpipe For Fuel Type1'],
                combined_mpg_for_fuel_type1=row['Combined Mpg For Fuel Type1'],
                unrounded_combined_mpg_for_fuel_type1=row['Unrounded Combined Mpg For Fuel Type1'],
                combined_mpg_for_fuel_type2=row['Combined Mpg For Fuel Type2'],
                unrounded_combined_mpg_for_fuel_type2=row['Unrounded Combined Mpg For Fuel Type2'],
                combined_electricity_consumption=row['Combined electricity consumption'],
                combined_gasoline_consumption=row['Combined gasoline consumption'],
                epa_combined_utility_factor=row['EPA combined utility factor'],
                cylinders=None if pd.isna(row['Cylinders']) else int(row['Cylinders']),
                engine_displacement=row['Engine displacement'],
                drive=row['Drive'],
                epa_model_type_index=row['EPA model type index'],
                engine_descriptor=row['Engine descriptor'],
                epa_fuel_economy_score=None if pd.isna(row['EPA Fuel Economy Score']) else int(row['EPA Fuel Economy Score']),
                annual_fuel_cost_for_fuel_type1=row['Annual Fuel Cost For Fuel Type1'],
                annual_fuel_cost_for_fuel_type2=row['Annual Fuel Cost For Fuel Type2'],
                fuel_type=row['Fuel Type'],
                fuel_type1=row['Fuel Type1'],
                ghg_score=None if pd.isna(row['GHG Score']) else int(row['GHG Score']),
                ghg_score_alternative_fuel=None if pd.isna(row['GHG Score Alternative Fuel']) else int(row['GHG Score Alternative Fuel']),
                highway_mpg_for_fuel_type1=row['Highway Mpg For Fuel Type1'],
                unrounded_highway_mpg_for_fuel_type1=row['Unrounded Highway Mpg For Fuel Type1'],
                highway_mpg_for_fuel_type2=row['Highway Mpg For Fuel Type2'],
                unrounded_highway_mpg_for_fuel_type2=row['Unrounded Highway Mpg For Fuel Type2'],
                highway_gasoline_consumption=row['Highway gasoline consumption'],
                highway_electricity_consumption=row['Highway electricity consumption'],
                epa_highway_utility_factor=row['EPA highway utility factor'],
                hatchback_luggage_volume=row['Hatchback luggage volume'],
                hatchback_passenger_volume=row['Hatchback passenger volume'],
                two_door_luggage_volume=row['2 door luggage volume'],
                four_door_luggage_volume=row['4 door luggage volume'],
                mpg_data=row['MPG Data'],
                phev_blended=row['PHEV Blended'],
                two_door_passenger_volume=row['2-door passenger volume'],
                four_door_passenger_volume=row['4-door passenger volume'],
                range_for_fuel_type1=row['Range For Fuel Type1'],
                range_city_for_fuel_type1=row['Range  City For Fuel Type1'],
                range_city_for_fuel_type2=row['Range  City For Fuel Type2'],
                range_highway_for_fuel_type1=row['Range  Highway For Fuel Type1'],
                range_highway_for_fuel_type2=row['Range  Highway For Fuel Type2'],
                transmission=row['Transmission'],
                unadjusted_city_mpg_for_fuel_type1=row['Unadjusted City Mpg For Fuel Type1'],
                unadjusted_city_mpg_for_fuel_type2=row['Unadjusted City Mpg For Fuel Type2'],
                unadjusted_highway_mpg_for_fuel_type1=row['Unadjusted Highway Mpg For Fuel Type1'],
                unadjusted_highway_mpg_for_fuel_type2=row['Unadjusted Highway Mpg For Fuel Type2'],
                vehicle_size_class=row['Vehicle Size Class'],
                year=row.get('Year', None),
                you_save_spend=row['You Save/Spend'],
                guzzler=row['Guzzler'],
                transmission_descriptor=row['Transmission descriptor'],
                t_charger=row['T Charger'],
                s_charger=row['S Charger'],
                atv_type=row['ATV Type'],
                fuel_type2=row['Fuel Type2'],
                epa_range_for_fuel_type2=row['Epa Range For Fuel Type2'],
                electric_motor=row['Electric motor'],
                mfr_code=row['MFR Code'],
                c240dscr=row['c240Dscr'],
                charge240b=row['charge240b'],
                c240b_dscr=row['C240B Dscr'],
                created_on=parse_datetime(row['Created On']).date() if pd.notna(row['Created On']) else None,
                modified_on=parse_datetime(row['Modified On']).date() if pd.notna(row['Modified On']) else None,
                start_stop=row['Start-Stop'] == 'Y',
                phev_city=row.get('PHEV City', None),
                phev_highway=row.get('PHEV Highway', None),
                phev_combined=row.get('PHEV Combined', None),
                base_model=row.get('baseModel', None)
            )
            vehicles.append(vehicle)

        Vehicle.objects.bulk_create(vehicles)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(vehicles)} vehicles.'))