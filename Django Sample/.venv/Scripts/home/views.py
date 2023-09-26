from django.shortcuts import render
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
    

# Substituted for HomeView class above
# def home(request):
#     # Brackets is a way of passing info from view to template
#     return render(request, 'home/welcome.html', {'today': datetime.today()})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})