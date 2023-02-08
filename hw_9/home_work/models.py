from django.db import models


# Create your models here.


def age(age):
    return [(i, i,) for i in range(1, age + 1)]


class HomeWork(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    age = models.IntegerField(verbose_name='Возраст', choices=age(18), default=1)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Home work'
        verbose_name_plural = 'Home work'