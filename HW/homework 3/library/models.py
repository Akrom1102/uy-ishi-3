from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"Title: {self.title} Author: {self.author} Number of books: {self.count}"
