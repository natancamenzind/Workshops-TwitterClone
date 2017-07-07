from django.conf.urls import url
from twitter_messages import views

app_name = 'twitter_messages'

urlpatterns = [
    url(r'^message_add/', views.MessageCreateView.as_view(), name='message-add'),
    url(r'^message_list/', views.MessageListView.as_view(), name="message-list" ),
    url(r'^message_detail/(?P<pk>(\d)+)', views.MessageDetailView.as_view(), name="message-detail" ),
]
