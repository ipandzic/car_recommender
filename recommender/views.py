import os

from django.conf import settings
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer
import openai
from django.http import JsonResponse
from rest_framework.decorators import api_view

from openai import OpenAI

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


@api_view(['POST'])
def chat_with_ai(request):
    user_input = request.data.get('message')
    if not user_input:
        return JsonResponse({"error": "No input provided"}, status=400)

    openai.api_key = settings.OPENAI_API_KEY

    client = OpenAI(
        api_key=openai.api_key,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
    )

    return JsonResponse({"response": completion.choices[0].message.content.strip()})
