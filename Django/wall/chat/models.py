from django.db import models
from login_app.models import User

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message by {self.user.first_name} at {self.created_at}'
