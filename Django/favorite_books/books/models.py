from django.db import models
from login_app.models import User 

class BookManager(models.Manager):
    def validate(self, data, id=None):
        errors = {}
        
        title = data.get('title', '').strip()
        description = data.get('description', '').strip()

        if not title:
            errors['title'] = 'Title field is required'
        elif len(title) < 2:  
            errors['title'] = 'Title must be at least 2 characters'
        elif self.filter(title=title).exclude(id=id).exists():
            errors['title'] = 'Title already exists'

        if not description:
            errors['description'] = "Description field is required"
        elif len(description) < 5:
            errors['description'] = "Description must be at least 5 characters"

        return errors
  
    def create_book(self, user, title, description):
        return self.create(
            title=title.strip(), 
            description=description.strip(), 
            uploaded_by=user
        )
    
    def update_book(self, book, data):
        title = data.get('title', '').strip()
        description = data.get('description', '').strip()

        if title:
            book.title = title
        if description:
            book.description = description

        book.save()
        return book

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_books")
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    
    objects = BookManager()

    def __str__(self):
        return f"{self.title} (Uploaded by: {self.uploaded_by.first_name})"