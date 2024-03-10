from django.urls import path

from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.all_, name='all'),
    path('detail/<int:course_id>/', views.detail, name='detail'),
]
