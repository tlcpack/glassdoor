from django import forms

from core.models import Review, Company

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = '__all__'

class CompanyForm(forms.ModelForm):
  class Meta:
    model = Company
    fields = '__all__'