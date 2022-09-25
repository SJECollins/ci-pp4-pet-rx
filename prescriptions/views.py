from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from records.models import Record
from .models import Prescription
from .forms import PrescrForm


# Create your views here.


def add_prescrip(request, animal_id):
    """
    Create a new prescription.
    Args: animal_id - takes id of selected animal for ForeignKey in model.
    Saves current user as vet for ForeignKey in model.
    Returns a 204 success status as not returning content, user then closes
    modal to return to profile.
    """
    animal = get_object_or_404(Record, id=animal_id)
    if request.method == 'POST':
        form = PrescrForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                animal = Record.objects.get(id=animal_id)
            except Record.DoesNotExist:
                pass
            instance.animal = animal
            instance.vet = request.user
            instance.save()
            return HttpResponse(status=204)
    else:
        prescr_form = PrescrForm()
    context = {
        'animal': animal,
        'prescr_form': prescr_form
    }
    return render(request, 'prescriptions/add_prescrip.html', context)


def list_prescrip(request, animal_id):
    """
    Retrieves list of prescriptions to display.
    Args: animal_id - takes id of current animal to retrieve prescriptions.
    """
    prescrip_list = Prescription.objects.filter(animal=animal_id).all()
    context = {'prescrip_list': prescrip_list}
    return render(request, 'prescriptions/list_prescrip.html', context)


def vet_prescrip(request):
    """
    Retrieves list of prescriptions to display for current user on profile.
    """
    prescrip_list = Prescription.objects.filter(vet=request.user).all()
    context = {'prescrip_list': prescrip_list}
    return render(request, 'prescriptions/list_prescrip_vet.html', context)


def detail_prescrip(request, prescrip_id):
    """
    Retrieves prescription to display.
    Args: prescrip_id - takes id of selected prescription to populate page.
    """
    prescription = get_object_or_404(Prescription, id=prescrip_id)
    context = {'prescription': prescription, }
    return render(request, 'prescriptions/detail_prescrip.html', context)


def delete_prescrip(request, prescrip_id):
    """
    Deletes prescription.
    Args: prescrip_id - takes id of selected prescription tp delete.
    """
    presc = get_object_or_404(Prescription, id=prescrip_id)
    presc.delete()
    return render(request, 'prescriptions/delete_confirm.html')
