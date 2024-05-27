from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ManyToManyField(Author)
    publication_date = models.DateField(null=True, blank=True)
