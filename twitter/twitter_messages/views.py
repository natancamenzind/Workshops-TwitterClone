from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Message
from django.contrib.auth.models import User


# Create your views here.

class MessageListView(ListView):
    model = Message
    # template_name = "TEMPLATE_NAME"



class MessageCreateView(CreateView):
    model = Message
    fields = [
        'text',
        'sender',
        'receiver',
    ]
    template_name = "twitter_messages/message_form.html"


class MessageDetailView(DetailView):
    model = Message
    # template_name = "TEMPLATE_NAME"
