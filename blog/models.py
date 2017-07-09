from django.db import models #librerias de Django
from django.utils import timezone #librerias de Django


class Post(models.Model): #definicion de un objeto
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #definicion de una funcion
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #definicion de una funcion que regresa un caracter
        return self.title
