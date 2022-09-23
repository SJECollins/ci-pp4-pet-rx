from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from .forms import RecordForm, WeightForm, NoteForm
from .models import Record


def records(request):
    record_list = Record.objects.all()
    context = {'record_list': record_list}
    return render(request, 'records/records.html', context)


def record_search(request):
    query = request.GET.get('query')
    record_qs = Record.objects.all()
    if query is not None:
        args = Q(name__icontains=query) | Q(surname__icontains=query)
        record_qs = Record.objects.filter(args)
    context = {'record_list': record_qs, }
    return render(request, 'records/record_search.html', context)


def add_animal(request):

    context = {}
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records:records')

    else:
        form = RecordForm()
    context['record_form'] = form
    return render(request, 'records/add_animal.html', context)


def edit_animal(request, animal_id):
    record = Record.objects.get(id=animal_id)
    form = RecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('records:animal_profile', animal_id=animal_id)
    else:
        form = RecordForm(request.POST or None, instance=record)
    context = {
        'record': record,
        'edit_form': form
        }
    return render(request, 'records/edit_animal.html', context)


def update_weight(request, animal_id):
    record = Record.objects.get(id=animal_id)
    form = WeightForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return HttpResponse(status=204)
    else:
        form = WeightForm(request.POST or None, instance=record)
    context = {
        'record': record,
        'update_weight': form,
    }
    return render(request, 'records/update_weight.html', context)


def edit_notes(request, animal_id):
    record = Record.objects.get(id=animal_id)
    form = NoteForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return HttpResponse(status=204)
    else:
        form = NoteForm(request.POST or None, instance=record)
    context = {
        'record': record,
        'edit_notes': form,
    }
    return render(request, 'records/edit_notes.html', context)


class AnimalRecord(View):

    def get(self, request, animal_id):
        queryset = Record.objects.all()
        profile = get_object_or_404(queryset, id=animal_id)

        context = {
            'profile': profile,
        }
        return render(request, 'records/animal_profile.html', context)
