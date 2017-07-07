from django.shortcuts import render , redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import UserLoginForm
# Create your views here.

class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        ctx = {'form': form}
        return render(
            request,
            'user_login_form.html',
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
                'user_login_form.html',
                {'form': form}
            )
