from django.db import models
from courses.models import Course


class Exercise(models.Model):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Курс')
    question = models.TextField(verbose_name='Вопрос')
    option1 = models.CharField(max_length=100, verbose_name='Вариант ответа 1')
    option2 = models.CharField(max_length=100, verbose_name='Вариант ответа 2')
    option3 = models.CharField(max_length=100, verbose_name='Вариант ответа 3')
    correct_option = models.CharField(max_length=100, verbose_name='Правильный ответ')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'exercise'
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.question
