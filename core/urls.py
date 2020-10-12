from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:post_id>/reviews', views.CompanyReviews, name='reviews'),
  path('create', views.CreateReview, name='create_review'),
  path('add_company', views.AddCompany, name='add_company'),
  # path()
]