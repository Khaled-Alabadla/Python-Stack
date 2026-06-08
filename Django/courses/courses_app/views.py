from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Course, CourseDescription, Comment

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def create_course(request):
    errors = {}
    if request.method == 'POST':
        errors = Course.objects.validate_course(request.POST.get('name'), request.POST.get('description'))
        if not errors:
            name = request.POST.get('name')
            description = request.POST.get('description')
            Course.objects.create_course(name=name, description=description)
            return redirect('course_list')
    courses = Course.objects.all()
    return render(request, 'course_list.html', {
        'courses': courses,
        'errors': errors if errors else None,
    })

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    description = CourseDescription.objects.get(course=course)
    comments = course.comments.order_by('-date')
    return render(request, 'course_detail.html', {
        'course': course,
        'description': description,
        'comments': comments,
    })

def delete_course(request, pk):
    if request.method == 'POST':
        Course.objects.delete_course(pk)
        return redirect('course_list')
    return render(request, 'confirm_delete.html', {'course': Course.objects.get(pk=pk)})

def add_comment(request, pk):
    course = Course.objects.get(pk=pk)
    description = CourseDescription.objects.get(course=course)
    comments = course.comments.order_by('-date')
    if request.method == 'POST':
        content = request.POST.get('content')
        course.comments.create(content=content)
        return redirect('add_comment', pk=pk)
    return render(request, 'course_detail.html', {
        'course': course,
        'description': description,
        'comments': comments,
    })

def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    course_pk = comment.course.pk
    if request.method == 'POST':
        comment.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'commentId': pk})
        return redirect('add_comment', pk=course_pk)
    return render(request, 'confirm_delete_comment.html', {'comment': comment})