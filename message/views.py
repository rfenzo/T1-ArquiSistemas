from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests import get

from .models import Message
from .forms import MessageForm

def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            ip = get('https://api.ipify.org').text
            new_message = Message(message=request.POST['message'], ip=ip)
            new_message.save()
            return redirect('index')
    else:
        form = MessageForm()

    messages = Message.objects.order_by('-date_added')
    context = {'messages':messages, 'form':form}
    return render(request, 'message/index.html', context)

