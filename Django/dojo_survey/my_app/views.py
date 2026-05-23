from django.shortcuts import render

def index(request):
    # Show a form on GET
    return render(request, 'index.html')


def result(request):
    # Extract submitted form data
    context = {
        'name': request.POST.get('name', ''),
        'dojo_location': request.POST.get('dojo_location', ''),
        'favorite_language': request.POST.get('favorite_language', ''),
        'comment': request.POST.get('comment', ''),
        # checkboxes may return multiple values
        'languages_known': request.POST.getlist('languages_known'),
    }
    return render(request, 'result.html', context)
