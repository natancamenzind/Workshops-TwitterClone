from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.UserLoginView.as_view(), name='login'),
    url(r'^logout/',views.UserLogoutView.as_view(), name='logout'),
    url(r'^create/', views.UserCreateView.as_view(), name ='create'),

]

