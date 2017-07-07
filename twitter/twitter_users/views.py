from django.shortcuts import render , redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import UserLoginForm, UserCreateForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        ctx = {'form': form}
        return render(
            request,
            'twitter_users/user_login_form.html',
            ctx
        )

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('/')
        else:
            return render(
                request,
                'twitter_users/user_login_form.html',
                {'form': form}
            )

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "twitter_users/user_form.html"
    success_url = reverse_lazy('/')


class UserLogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')
        else:
            return redirect('login')


