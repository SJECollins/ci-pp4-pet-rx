from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import RecordForm
from .models import Record


def records(request):
    record_list = Record.objects.all()
    context = {'record_list': record_list}
    return render(request, 'records/records.html', context)


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
