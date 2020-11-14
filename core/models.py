import math

from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
  name = models.TextField(max_length=100)
  address = models.TextField(max_length=100)
  website = models.URLField()

  def get_absolute_url(self):
    return reverse('company-detail', args=[str(self.id)])

  def __str__(self):
    return self.name
  


class Review(models.Model):
    company = models.ForeignKey('Company', related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])

    def get_absolute_url(self):
      return reverse('reviews', args=[str(self.id)])

    def __str__(self):
        return f"{self.company!r} - {self.rating!r}"