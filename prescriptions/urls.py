from django.urls import path
from . import views

app_name = 'prescriptions'
urlpatterns = [
    path('add_prescrip/<int:id>', views.add_prescrip, name='add_prescrip'),
    path('view_prescrip/', views.view_prescrip, name='view_prescrip'),
    path('prescriplist/', views.PrescripList.as_view(), name='prescriplist'),
]
