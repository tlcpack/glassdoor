from django.shortcuts import render
from django.views import generic
from .models import Company, Review

# Create your views here.
def index(request):
  companies = Company.objects.all()
  return render(request, 'index.html', { 'companies': companies})