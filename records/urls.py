from django.urls import path
from . import views

app_name = 'records'
urlpatterns = [
    path('records/', views.records, name='records'),
    path('add-animal/', views.add_animal, name='add_animal'),
    path('animal-profile/<int:id>', views.AnimalRecord.as_view(), name='animal_profile'),
    path('edit-animal/<int:id>', views.edit_animal, name='edit_animal'),
]
