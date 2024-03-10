from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание курса')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'course'
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title
