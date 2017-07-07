"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from twitter_comments import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^twitter/', views.TwitterBaseView.as_view(), name="base"),
    url(r'^twitter_users/', include('twitter_users.urls')),
    url(r'^twitter_entries/', include('twitter_entries.urls')),
    url(r'^twitter_comments/', include('twitter_comments.urls')),
    url(r'^twitter_messages/', include('twitter_messages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)