from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    visits = request.session.get('visits', 0) + 1
    request.session['visits'] = visits

    counter = request.session.get('counter', 0)

    if request.method == 'POST':
        increment_value = request.POST.get('increment_value', '1')
        try:
            increment_amount = int(increment_value)
        except (ValueError, TypeError):
            increment_amount = 1

        counter += increment_amount
        request.session['counter'] = counter
        return redirect(reverse('index'))

    return render(request, 'counter/index.html', {'visits': visits, 'counter': counter})


def destroy_session(request):
    request.session.flush()
    return redirect('index')


def increment2(request):
    request.session['counter'] = request.session.get('counter', 0) + 2
    return redirect('index')
