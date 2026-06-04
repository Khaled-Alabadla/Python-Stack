from django.shortcuts import render, redirect, get_object_or_404
from .models import Show


def index(request):
	shows = Show.objects.all().order_by('id')
	return render(request, 'tv_shows_app/index.html', {'shows': shows})


def new(request):
	return render(request, 'tv_shows_app/new.html')


def create(request):
	if request.method == 'POST':
		title = request.POST.get('title', '').strip()
		network = request.POST.get('network', '').strip()
		release_date = request.POST.get('release_date') or None
		description = request.POST.get('description', '').strip()
		show = Show.objects.create(
			title=title,
			network=network,
			release_date=release_date,
			description=description,
		)
		return redirect('/shows/')
	return redirect('/shows/new')


def show(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	return render(request, 'tv_shows_app/show.html', {'show': show})


def edit(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	return render(request, 'tv_shows_app/edit.html', {'show': show})


def update(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	if request.method == 'POST':
		show.title = request.POST.get('title', show.title).strip()
		show.network = request.POST.get('network', show.network).strip()
		rd = request.POST.get('release_date')
		show.release_date = rd or None
		show.description = request.POST.get('description', show.description).strip()
		show.save()
	return redirect('/shows/')


def destroy(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	if request.method == 'POST':
		show.delete()
	return redirect('/shows/')
