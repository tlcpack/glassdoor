from django.db import models

# Create your models here.
class Company(models.Model):
  name = 
  address = 
  website = 

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