from django.shortcuts import render
from django.views.generic import View
from .models import Menu


class IndexView(View):

    def get(self, request):
        return render(request=request, template_name='base.html')