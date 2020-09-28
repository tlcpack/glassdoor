from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
  name = models.TextField()
  address = models.TextField()
  website = models.URLField()

  def __str__(self):
    return self.name
  


class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])

    class Meta:
        unique_together = ('user', 'company')

    def __str__(self):
        return f"{self.user!r} - {self.company!r}"