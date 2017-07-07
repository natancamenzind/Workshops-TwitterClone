from django.shortcuts import render

# Create your views here.
from django.views import View


class TwitterBaseView(View):

    def get(self,request):

        return render(request, 'twitter/base.html')






