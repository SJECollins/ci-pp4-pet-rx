from django.urls import path
from . import views

app_name = 'records'
urlpatterns = [
    path('records/', views.records, name='records'),
    path('add-animal/', views.add_animal, name='add_animal'),
]
