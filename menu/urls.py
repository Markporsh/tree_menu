from .views import menu
from django.urls import path


urlpatterns = [
    path('', menu, name='menu'),
    path('<slug:slug>/', menu, name='menu'),
]
