from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count

from .models import Dojo, Ninja


def index(request):
  dojos = Dojo.objects.all()
  return render(request, 'dojo_app/index.html', {
        'dojos': dojos,
    })


def create_dojo(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        city = request.POST.get('city', '').strip()
        state = request.POST.get('state', '').strip().upper()
        if name and city and state:
            Dojo.objects.create(name=name, city=city, state=state)
    return redirect('index')


def create_ninja(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        dojo_id = request.POST.get('dojo')
        if first_name and last_name and dojo_id:
            dojo = get_object_or_404(Dojo, pk=dojo_id)
            Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('index')


def delete_dojo(request, dojo_id):
    if request.method == 'POST':
        dojo = get_object_or_404(Dojo, pk=dojo_id)
        dojo.delete()
    return redirect('index')
