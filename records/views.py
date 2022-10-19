from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from petrx.decorators import vet_login_and_active
from .forms import RecordForm, WeightForm, NoteForm
from .models import Record


@vet_login_and_active
def records(request):
    """
    Retrieve list of records to display, paginated
    Pagination from official docs, see link in README credits
    """
    record_list = Record.objects.all()
    paginator = Paginator(record_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'record_list': record_list,
        'page_obj': page_obj
    }
    return render(request, 'records/records.html', context)


@vet_login_and_active
def record_search(request):
    """
    Function to search records: retrieves records by name or surname matching
    query.
    From Codemy.com, see link in README credits
    """
    query = request.GET.get('query')
    record_qs = []
    record_list = Record.objects.all()
    if query is not None:
        args = Q(name__icontains=query) | Q(surname__icontains=query)
        record_qs = Record.objects.filter(args)
    context = {
        'record_list': record_list,
        'record_search': record_qs}
    return render(request, 'records/record_search.html', context)


@vet_login_and_active
def add_animal(request):
    """
    Create a new animal record.
    Redirects user back to records page.
    """
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records:records')
    else:
        form = RecordForm()
    context = {'record_form': form}
    return render(request, 'records/add_animal.html', context)


@vet_login_and_active
def edit_animal(request, animal_id):
    """
    Edit animal record.
    Args: animal_id - takes id of selected animal's record for initial data
    on form.
    Redirects user to animal's profile
    """
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


@vet_login_and_active
def update_weight(request, animal_id):
    """
    Edit animal's weight only.
    Args: animal_id - takes id of selected animal's record for intial weight
    on form.
    Returns a 204 success status as not returning content, user then closes
    modal to return to profile.
    """
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


@vet_login_and_active
def edit_notes(request, animal_id):
    """
    Edit notes for animal on record.
    Args: animal_id - takes id of selected animal's record for initial data in
    notes.
    Returns a 204 success status as not returning content, user then closes
    modal to return to profile.
    """
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
    """
    Displays animal's record.
    Args: animal_id - takes id of selected animal to retrieve record.
    Get method: retrieves record and renders animal's profile
    """
    @method_decorator(vet_login_and_active)
    def get(self, request, animal_id):
        queryset = Record.objects.all()
        profile = get_object_or_404(queryset, id=animal_id)
        context = {'profile': profile}
        return render(request, 'records/animal_profile.html', context)
