from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User


def index(request):
	users = User.objects.all().order_by('id')
  
	return render(request, 'user_app/users.html', {'users': users})


def create_user(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name', '').strip()
		last_name = request.POST.get('last_name', '').strip()
		email_address = request.POST.get('email_address', '').strip()
		age = request.POST.get('age', '').strip()

		try:
			age_val = int(age)
		except (ValueError, TypeError):
			age_val = 0

		User.objects.create(
			first_name=first_name,
			last_name=last_name,
			email_address=email_address,
			age=age_val,
		)

	return redirect(reverse('user_app:index'))
