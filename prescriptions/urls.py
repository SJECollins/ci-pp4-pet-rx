from django.urls import path
from . import views

app_name = 'prescriptions'
urlpatterns = [
     path('drugs/', views.drugs, name='drugs'),
     path('drug-search/', views.drug_search, name='drug_search'),
     path('detail-drug/<int:drug_id>', views.detail_drug, name='detail_drug'),
     path('add-prescrip/<int:animal_id>', views.add_prescrip,
          name='add_prescrip'),
     path('drug-choices/', views.drug_choices, name='drug_choices'),
     path('delete-prescrip/<int:prescrip_id>', views.delete_prescrip,
          name='delete_prescrip'),
     path('edit-prescrip/<int:prescrip_id>', views.edit_prescrip,
          name='edit_prescrip'),
     path('list-prescrip/<int:animal_id>', views.list_prescrip,
          name='list_prescrip'),
     path('vet-prescrip/', views.vet_prescrip, name='vet_prescrip'),
     path('detail-prescrip/<int:prescrip_id>', views.detail_prescrip,
         name='detail_prescrip'),
]
