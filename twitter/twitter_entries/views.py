from django.views.generic import ListView, CreateView
from .models import Tweet
from .forms import TweetCreateForm


class TwitterListView(ListView):

    model = Tweet


class TweetCreateView(CreateView):

    form_class= TweetCreateForm
    success_url = '/twitter/'
    template_name = 'twitter_entries/tweet_form.html'
