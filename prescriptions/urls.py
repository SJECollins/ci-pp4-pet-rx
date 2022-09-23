from django.urls import path
from . import views

app_name = 'prescriptions'
urlpatterns = [
    path('add-prescrip/<int:animal_id>', views.add_prescrip, name='add_prescrip'),
    path('delete-prescrip/<int:prescrip_id>', views.delete_prescrip, name='delete_prescrip'),
    path('list-prescrip/<int:animal_id>', views.list_prescrip, name='list_prescrip'),
    path('vet-prescrip/', views.vet_prescrip, name='vet_prescrip'),
    path('detail-prescrip/<int:prescrip_id>', views.detail_prescrip, name='detail_prescrip')
]
