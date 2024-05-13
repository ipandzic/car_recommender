from django.conf import settings
from .models import Vehicle
import openai
from django.http import JsonResponse
from rest_framework.decorators import api_view

from openai import OpenAI


def get_recommended_vehicles(user_input):
    # Parsing the user input for keywords and key phrases that help in filtering the Vehicle data.
    queries = {
        'fuel efficient': Vehicle.objects.filter(city_mpg_for_fuel_type1__gte=30),  # Vehicles with good fuel efficiency
        'bmw': Vehicle.objects.filter(make="BMW"),
        'SUV': Vehicle.objects.filter(vehicle_size_class="SUV"),  # SUV type vehicles
        'electric': Vehicle.objects.filter(fuel_type__icontains='electric'),  # Electric vehicles
        'sedan': Vehicle.objects.filter(vehicle_size_class="Sedan"),  # Sedan type vehicles
        'luxury': Vehicle.objects.filter(engine_descriptor__icontains='turbo'),  # Luxury vehicles generally have turbo engines
        'cheap': Vehicle.objects.filter(annual_fuel_cost_for_fuel_type1__lte=1000),  # Assuming 'cheap' relates to low fuel cost
        'spacious': Vehicle.objects.filter(hatchback_passenger_volume__gte=100)  # Vehicles with a large passenger volume
    }

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
    for vehicle in vehicles[:10]:
        message += f"- {vehicle.make} {vehicle.model}, MPG: {vehicle.city_mpg_for_fuel_type1}, " \
                   f"Price: ${vehicle.annual_fuel_cost_for_fuel_type1}, Engine: {vehicle.engine_descriptor}, " \
                   f"Fuel Type: {vehicle.fuel_type}, CO2 Emissions: {vehicle.co2_tailpipe_for_fuel_type1} g/km\n"
    return message


@api_view(['POST'])
def chat_with_ai(request):
    user_input = request.data.get('message', '')
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
            {"role": "system", "content": "You are a helpful car recommendation assistant. Focus on providing "
                                          "information and recommendations related to cars and avoid unrelated "
                                          "topics."},
            {"role": "assistant", "content": vehicle_message},
            {"role": "user", "content": user_input},
        ]
    )

    return JsonResponse({"response": completion.choices[0].message.content.strip()})
