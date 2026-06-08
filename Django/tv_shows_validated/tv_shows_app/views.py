from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *


def index(request):
	shows = Show.objects.all().order_by('id')
	return render(request, 'tv_shows_app/index.html', {'shows': shows})


def new(request):
	return render(request, 'tv_shows_app/new.html')


def create(request):
	if request.method == 'POST':
		errors = Show.objects.create_validator(request.POST)
		if errors:
			for field, message in errors.items():
				messages.error(request, message)
			return redirect('/shows/new')
		
		Show.objects.add_show(request.POST)
		return redirect('/shows/')
	return redirect('/shows/new')


def show(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	return render(request, 'tv_shows_app/show.html', {'show': show})

def edit(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	formatted_date = ""
	if show.release_date:
		formatted_date = show.release_date.strftime('%Y-%m-%d')

	return render(request, 'tv_shows_app/edit.html', {'show': show, 'formatted_date': formatted_date})


def update(request, show_id):
	errors = Show.objects.edit_validator(request.POST, show_id)
	if errors:
		for field, message in errors.items():
			messages.error(request, message)
		return redirect(f'/shows/{show_id}/edit')

	Show.objects.update_show(request.POST, show_id)
	return redirect('/shows/')


def destroy(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	if request.method == 'POST':
		show.delete()
	return redirect('/shows/')
