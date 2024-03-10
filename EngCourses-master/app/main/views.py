from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'EngCourses - Главная',
        'content': "EngCourses - продвинутые курсы по изучению иностранных языков"
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'EngCourses - О нас',
        'content': "О нас",
        'text_on_page': "Мы - команда профессиональных преподавателей и разработчиков, "
                        "которые объединились, чтобы создать инновационную платформу для "
                        "обучения иностранным языкам. Наша цель - предоставить студентам "
                        "интеллектуальные и технологически продвинутые инструменты для "
                        "эффективного освоения новых языков."
    }

    return render(request, 'main/about.html', context)
