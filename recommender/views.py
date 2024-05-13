from django.conf import settings
from .models import Vehicle
import openai
from django.http import JsonResponse
from rest_framework.decorators import api_view

from openai import OpenAI


def get_recommended_vehicles(user_input):
    make_list = [
        "S and S Coach Company  E.p. Dutton",
        "Ford",
        "Maserati",
        "Dodge",
        "Excalibur Autos",
        "Infiniti",
        "J.K. Motors",
        "Fisker",
        "TVR Engineering Ltd",
        "RUF Automobile",
        "Grumman Allied Industries",
        "CODA Automotive",
        "Dacia",
        "SRT",
        "PAS Inc - GMC",
        "ASC Incorporated",
        "Audi",
        "Mcevoy Motors",
        "Import Trade Services",
        "Lexus",
        "Import Foreign Auto Sales Inc",
        "Isis Imports Ltd",
        "General Motors",
        "Jeep",
        "Vector",
        "American Motors Corporation",
        "Cadillac",
        "Sterling",
        "Autokraft Limited",
        "Texas Coach Company",
        "Panther Car Company Limited",
        "Evans Automobiles",
        "Ferrari",
        "GMC",
        "Maybach",
        "Lincoln",
        "Honda",
        "Spyker",
        "Chevrolet",
        "JBA Motorcars, Inc.",
        "Daihatsu",
        "Quantum Technologies",
        "Environmental Rsch and Devp Corp",
        "Porsche",
        "Pininfarina",
        "Rolls-Royce",
        "Tesla",
        "Jaguar",
        "Renault",
        "Kia",
        "Saleen Performance",
        "CX Automotive",
        "Ruf Automobile Gmbh",
        "Pagani",
        "Bugatti",
        "McLaren Automotive",
        "Fiat",
        "Rivian",
        "Buick",
        "Kandi",
        "Merkur",
        "CCC Engineering",
        "Mercury",
        "Wallace Environmental",
        "Roush Performance",
        "Toyota",
        "Bertone",
        "Mahindra",
        "Grumman Olson",
        "Avanti Motor Corporation",
        "VPG",
        "BMW Alpina",
        "PAS, Inc",
        "Federal Coach",
        "MINI",
        "Bentley",
        "Vinfast",
        "Peugeot",
        "Pontiac",
        "Plymouth",
        "Koenigsegg",
        "Lambda Control Systems",
        "Volvo",
        "Panoz Auto-Development",
        "Acura",
        "Polestar",
        "Suzuki",
        "BYD",
        "Bitter Gmbh and Co. Kg",
        "Aston Martin",
        "Mitsubishi",
        "AM General",
        "E. P. Dutton, Inc.",
        "Qvale",
        "Chrysler",
        "London Taxi",
        "Isuzu",
        "Mobility Ventures LLC",
        "Ram",
        "Daewoo",
        "Morgan",
        "Panos",
        "Scion",
        "Shelby",
        "Saturn",
        "Bill Dovell Motor Car Company",
        "Vixen Motor Company",
        "Karma",
        "Lordstown",
        "Lucid",
        "Alfa Romeo",
        "smart",
        "Lotus",
        "Lamborghini",
        "Mercedes-Benz",
        "Oldsmobile",
        "Goldacre",
        "Superior Coaches Div E.p. Dutton",
        "Consulier Industries Inc",
        "Land Rover",
        "STI",
        "Nissan",
        "Kenyon Corporation Of America",
        "Genesis",
        "Aurora Cars Ltd",
        "Saab",
        "Hyundai",
        "Yugo",
        "London Coach Co Inc",
        "Saleen",
        "Geo",
        "Subaru",
        "Laforza Automobile Inc",
        "Tecstar, LP",
        "Mazda",
        "Red Shift Ltd.",
        "BMW",
        "Volkswagen",
        "Eagle",
        "Azure Dynamics",
        "Hummer",
        "Dabryan Coach Builders Inc",
        "Volga Associated Automobile",
    ]

    # Parsing the user input for keywords and key phrases that help in filtering the Vehicle data.
    queries = {
        "fuel efficient": Vehicle.objects.filter(
            city_mpg_for_fuel_type1__gte=30
        ),  # Vehicles with good fuel efficiency
        "SUV": Vehicle.objects.filter(vehicle_size_class="SUV"),  # SUV type vehicles
        "electric": Vehicle.objects.filter(
            fuel_type__icontains="electric"
        ),  # Electric vehicles
        "sedan": Vehicle.objects.filter(
            vehicle_size_class="Sedan"
        ),  # Sedan type vehicles
        "luxury": Vehicle.objects.filter(
            engine_descriptor__icontains="turbo"
        ),  # Luxury vehicles generally have turbo engines
        "cheap": Vehicle.objects.filter(
            annual_fuel_cost_for_fuel_type1__lte=1000
        ),  # Assuming 'cheap' relates to low fuel cost
        "spacious": Vehicle.objects.filter(
            hatchback_passenger_volume__gte=100
        ),  # Vehicles with a large passenger volume
    }

    queries_with_distinct_makes = {
        make.lower(): Vehicle.objects.filter(make=make) for make in make_list
    }

    # Now merge this new dictionary to existing `queries` dictionary
    queries.update(queries_with_distinct_makes)

    # If user input is complex, consider using NLP techniques or regex to more accurately extract features.
    for keyword, query in queries.items():
        if keyword in user_input.lower():
            return query  # Return the first relevant query

    # If none of the specific keywords are found, you can default to some kind of default recommendation, or return none
    return Vehicle.objects.none()


def format_vehicles_for_chat(vehicles):
    if not vehicles:
        return "I couldn't find any vehicles matching your criteria."
    message = "Here is information from the NHTSA Product Information Catalog Vehicle Listing:\n"
    for vehicle in vehicles[:20]:

        message += (
            f"- {vehicle.make} {vehicle.model}, MPG: {vehicle.city_mpg_for_fuel_type1}, "
            f"Price: ${vehicle.annual_fuel_cost_for_fuel_type1}, Engine: {vehicle.engine_descriptor}, "
            f"Fuel Type: {vehicle.fuel_type}, CO2 Emissions: {vehicle.co2_tailpipe_for_fuel_type1} g/km\n"
        )
    return message


@api_view(["POST"])
def chat_with_ai(request):
    user_input = request.data.get("message", "")
    if not user_input:
        return JsonResponse({"error": "No input provided"}, status=400)

    recommended_vehicles = get_recommended_vehicles(user_input)
    vehicle_message = format_vehicles_for_chat(recommended_vehicles)

    openai.api_key = settings.OPENAI_API_KEY

    client = OpenAI(
        api_key=openai.api_key,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful car recommendation assistant. Focus on providing "
                "information and recommendations related to cars and avoid unrelated "
                "topics.",
            },
            {"role": "assistant", "content": vehicle_message},
            {"role": "user", "content": user_input},
        ],
    )


    return JsonResponse({"response": completion.choices[0].message.content.strip()})
