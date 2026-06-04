from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=45, blank=True)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title
