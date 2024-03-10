from courses.models import Course
from django.shortcuts import render, get_object_or_404, redirect
from exercises.models import Exercise
from django.contrib import messages


def all_(request):
    courses = Course.objects.all()
    context = {
        'title': 'EngCourses - Все курсы',
        'courses': courses
    }
    return render(request, 'courses/all.html', context)


def detail(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    user = request.user

    if user.is_authenticated:
        exercises = Exercise.objects.filter(course_id=course_id).all()
        context = {
            'title': f'EngCourses - {course.title}',
            'course': course,
            'exercises': exercises,
        }
        return render(request, 'courses/detail.html', context)

    messages.warning(request, f"Авторизуйтесь для доступа к курсу")
    return redirect(request.META['HTTP_REFERER'])
