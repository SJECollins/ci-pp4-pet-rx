from django.urls import path
from . import views

app_name = 'prescriptions'
urlpatterns = [
    path('add_prescrip/<int:id>', views.add_prescrip, name='add_prescrip'),
    path('view_prescrip/<int:id>', views.view_prescrip, name='view_prescrip'),
    path('vet_prescrip/', views.vet_prescrip, name='vet_prescrip'),
    path('prescriplist/', views.PrescripList.as_view(), name='prescriplist'),
]
