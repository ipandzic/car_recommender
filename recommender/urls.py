from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, chat_with_ai

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', chat_with_ai, name='chat-with-ai'),
]
