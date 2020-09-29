from django import forms

from core.models import Review

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = '__all__'