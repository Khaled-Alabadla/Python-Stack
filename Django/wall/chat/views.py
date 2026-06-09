from django.shortcuts import redirect, render, get_object_or_404
from .models import Message
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from login_app.models import *

def index(request):
  if 'user_id' not in request.session:
        return redirect('login')
  
  messages = Message.objects.all().order_by('-created_at')
  return render(request, 'chat/index.html', {'messages': messages})

def create_message(request):
  # check that the user is authenticated before allowing them to create a message
  if 'user_id' not in request.session:
        return redirect('login')
  
  if request.method == 'POST':
    message_content = request.POST.get('message')
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    Message.objects.create(message=message_content, user=user)
    return redirect('chat:messages_list')

  return render(request, 'chat/create.html')

def delete(request, pk):
     if 'user_id' not in request.session:
        return redirect('login')
  
     if request.method == 'POST':
        message = get_object_or_404(Message, pk=pk)
        now = timezone.now()
        thirty_minutes_ago = now - timedelta(minutes=30) 
        if request.session.get('user_id', 0) == message.user.id and message.created_at >= thirty_minutes_ago:
            message.delete()
            messages.success(request, "Message deleted successfully")
            return redirect('chat:messages_list')
        
        messages.error(request, "you can't delete message because it is cerated more than 30 minutes")
        return redirect('chat:messages_list')
            
