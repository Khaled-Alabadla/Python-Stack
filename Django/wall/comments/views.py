from django.shortcuts import render, redirect
from .models import *

def create(request):
  if not 'user_id' in request.session:
    return redirect('login')
  
  if request.method == 'POST':
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    message_id = request.POST.get('message', None)
    comment = request.POST.get('comment', '')
    message = Message.objects.get(id=message_id)
    Comment.objects.create(comment=comment, message=message, user=user)
    return redirect('chat:messages_list')



