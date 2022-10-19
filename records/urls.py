from django.urls import path
from . import views

app_name = 'records'
urlpatterns = [
    path('', views.records, name='records'),
    path('record-search/', views.record_search, name='record_search'),
    path('add-animal/', views.add_animal, name='add_animal'),
    path('animal-profile/<int:animal_id>', views.AnimalRecord.as_view(),
         name='animal_profile'),
    path('edit-animal/<int:animal_id>', views.edit_animal, name='edit_animal'),
    path('update-weight/<int:animal_id>', views.update_weight,
         name='update_weight'),
    path('edit-notes/<int:animal_id>', views.edit_notes, name='edit_notes'),
]
