from django.urls import path
from . import views

app_name = 'prescriptions'
urlpatterns = [
    path('add_prescrip/<int:id>', views.add_prescrip, name='add_prescrip'),
    path('delete_prescrip/<int:prescrip_id>', views.delete_prescrip, name='delete_prescrip'),
    path('list_prescrip/<int:id>', views.list_prescrip, name='list_prescrip'),
    path('vet_prescrip/', views.vet_prescrip, name='vet_prescrip'),
    # path('prescriplist/', views.PrescripList.as_view(), name='prescriplist'),
    path('view_prescrip/<int:id>', views.ViewPrescrip.as_view(), name='view_prescrip')
]
