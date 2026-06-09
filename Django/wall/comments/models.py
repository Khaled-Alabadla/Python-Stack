from django.db import models
from chat.models import Message
from login_app.models import User

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.first_name} on message {self.message.id} at {self.created_at}'