from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:post_id>/reviews', views.CompanyReviews, name='reviews'),
  path('create', views.CreateReview, name='create_review'),
  path('add_company', views.AddCompany, name='add_company'),
  path('<int:pk>/review_detail', views.ReviewDetailView.as_view(), name='review-detail'),
  path('<int:pk>/company_detail', views.CompanyDetailView.as_view(), name='company-detail')
]