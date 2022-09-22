from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from records.models import Record
from .models import Prescription
from .forms import PrescrForm


# Create your views here.


def add_prescrip(request, id):
    animal = get_object_or_404(Record, id=id)
    if request.method == 'POST':
        form = PrescrForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                animal = Record.objects.get(id=id)
            except Record.DoesNotExist:
                pass
            instance.animal = animal
            instance.vet = request.user
            instance.save()
            return redirect('records:animal_profile', id=id)
    else:
        prescr_form = PrescrForm()
    context = {
        'animal': animal,
        'prescr_form': prescr_form
    }
    return render(request, 'prescriptions/add_prescrip.html', context)


# def delete_prescrip(request, id):
#     presc = get_object_or_404(Prescription, id=id)
#     presc.delete()
#     return redirect('prescriptions:view_prescrip')


def list_prescrip(request, id):
    prescrip_list = Prescription.objects.filter(animal=id).all()
    context = {'prescrip_list': prescrip_list}
    return render(request, 'prescriptions/list_prescrip.html', context)


def vet_prescrip(request):
    prescrip_list = Prescription.objects.filter(vet=request.user).all()
    context = {'prescrip_list': prescrip_list}
    return render(request, 'prescriptions/list_prescrip.html', context)


class ViewPrescrip(View):

    def get(self, request, id):
        queryset = Prescription.objects.all()
        prescription = get_object_or_404(queryset, id=id)

        context = {
            'prescription': prescription,
        }
        return render(request, 'prescriptions/view_prescrip.html', context)
