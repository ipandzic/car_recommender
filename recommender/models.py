from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_type = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)


class Feature(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100)


class Vehicle(models.Model):
    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    annual_petroleum_consumption_for_fuel_type1 = models.FloatField(null=True, blank=True)
    annual_petroleum_consumption_for_fuel_type2 = models.FloatField(null=True, blank=True)
    time_to_charge_at_120v = models.IntegerField(null=True, blank=True)
    time_to_charge_at_240v = models.IntegerField(null=True, blank=True)
    city_mpg_for_fuel_type1 = models.IntegerField(null=True, blank=True)
    unrounded_city_mpg_for_fuel_type1 = models.FloatField(null=True, blank=True)
    city_mpg_for_fuel_type2 = models.IntegerField(null=True, blank=True)
    unrounded_city_mpg_for_fuel_type2 = models.FloatField(null=True, blank=True)
    city_gasoline_consumption = models.FloatField(null=True, blank=True)
    city_electricity_consumption = models.FloatField(null=True, blank=True)
    epa_city_utility_factor = models.FloatField(null=True, blank=True)
    co2_fuel_type1 = models.IntegerField(null=True, blank=True)
    co2_fuel_type2 = models.IntegerField(null=True, blank=True)
    co2_tailpipe_for_fuel_type2 = models.FloatField(null=True, blank=True)
    co2_tailpipe_for_fuel_type1 = models.FloatField(null=True, blank=True)
    combined_mpg_for_fuel_type1 = models.IntegerField(null=True, blank=True)
    unrounded_combined_mpg_for_fuel_type1 = models.FloatField(null=True, blank=True)
    combined_mpg_for_fuel_type2 = models.IntegerField(null=True, blank=True)
    unrounded_combined_mpg_for_fuel_type2 = models.FloatField(null=True, blank=True)
    combined_electricity_consumption = models.FloatField(null=True, blank=True)
    combined_gasoline_consumption = models.FloatField(null=True, blank=True)
    epa_combined_utility_factor = models.FloatField(null=True, blank=True)
    cylinders = models.IntegerField(null=True, blank=True)
    engine_displacement = models.FloatField(null=True, blank=True)
    drive = models.CharField(max_length=100, null=True, blank=True)
    epa_model_type_index = models.CharField(max_length=100, null=True, blank=True)
    engine_descriptor = models.CharField(max_length=100, null=True, blank=True)
    epa_fuel_economy_score = models.IntegerField(null=True, blank=True)
    annual_fuel_cost_for_fuel_type1 = models.IntegerField(null=True, blank=True)
    annual_fuel_cost_for_fuel_type2 = models.IntegerField(null=True, blank=True)
    fuel_type = models.CharField(max_length=100, null=True, blank=True)
    fuel_type1 = models.CharField(max_length=100, null=True, blank=True)
    ghg_score = models.IntegerField(blank=True, null=True)
    ghg_score_alternative_fuel = models.IntegerField(blank=True, null=True)
    highway_mpg_for_fuel_type1 = models.IntegerField(null=True, blank=True)
    unrounded_highway_mpg_for_fuel_type1 = models.FloatField(null=True, blank=True)
    highway_mpg_for_fuel_type2 = models.IntegerField(null=True, blank=True)
    unrounded_highway_mpg_for_fuel_type2 = models.FloatField(null=True, blank=True)
    highway_gasoline_consumption = models.FloatField(null=True, blank=True)
    highway_electricity_consumption = models.FloatField(null=True, blank=True)
    epa_highway_utility_factor = models.FloatField(null=True, blank=True)
    hatchback_luggage_volume = models.FloatField(null=True, blank=True)
    hatchback_passenger_volume = models.FloatField(null=True, blank=True)
    two_door_luggage_volume = models.FloatField(null=True, blank=True)
    four_door_luggage_volume = models.FloatField(null=True, blank=True)
    mpg_data = models.CharField(max_length=100, null=True, blank=True)
    phev_blended = models.BooleanField(null=True, blank=True)
    two_door_passenger_volume = models.IntegerField(null=True, blank=True)
    four_door_passenger_volume = models.IntegerField(null=True, blank=True)
    range_for_fuel_type1 = models.FloatField(null=True, blank=True)
    range_city_for_fuel_type1 = models.FloatField(null=True, blank=True)
    range_city_for_fuel_type2 = models.FloatField(null=True, blank=True)
    range_highway_for_fuel_type1 = models.FloatField(null=True, blank=True)
    range_highway_for_fuel_type2 = models.FloatField(null=True, blank=True)
    transmission = models.CharField(max_length=100, null=True, blank=True)
    unadjusted_city_mpg_for_fuel_type1 = models.FloatField(null=True, blank=True)
    unadjusted_city_mpg_for_fuel_type2 = models.FloatField(null=True, blank=True)
    unadjusted_highway_mpg_for_fuel_type1 = models.FloatField(null=True, blank=True)
    unadjusted_highway_mpg_for_fuel_type2 = models.FloatField(null=True, blank=True)
    vehicle_size_class = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    you_save_spend = models.IntegerField(null=True, blank=True)
    guzzler = models.CharField(max_length=100, blank=True, null=True)
    transmission_descriptor = models.CharField(max_length=100, blank=True, null=True)
    t_charger = models.CharField(max_length=100, blank=True, null=True)
    s_charger = models.CharField(max_length=100, blank=True, null=True)
    atv_type = models.CharField(max_length=100, blank=True, null=True)
    fuel_type2 = models.CharField(max_length=100, blank=True, null=True)
    epa_range_for_fuel_type2 = models.CharField(blank=True, null=True)
    electric_motor = models.CharField(max_length=100, blank=True, null=True)
    mfr_code = models.CharField(max_length=100, blank=True, null=True)
    c240dscr = models.CharField(max_length=100, blank=True, null=True)
    charge240b = models.FloatField(blank=True, null=True)
    c240b_dscr = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateField(null=True, blank=True)
    modified_on = models.DateField(null=True, blank=True)
    start_stop = models.BooleanField(null=True, blank=True)
    phev_city = models.IntegerField(null=True, blank=True)
    phev_highway = models.IntegerField(null=True, blank=True)
    phev_combined = models.IntegerField(null=True, blank=True)
    base_model = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
