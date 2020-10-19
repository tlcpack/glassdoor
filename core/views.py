from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Count
from django.views import generic
from .forms import ReviewForm, CompanyForm
from .models import Company, Review

# Create your views here.
def index(request):
  # companies = Company.objects.all()
  rating_averages = Company.objects.annotate(avg_rating=Avg('reviews__rating'))
  # review_average = Company.objects.all().aggregate(Avg('review'))
  # reviews = Review.objects.all()
  # rating_average = Review.objects.aggregate(Avg('rating'))
  # comp_reviews = Company.objects.annotate(number_reviews=Count('reviews'))
  return render(request, 'index.html', { 'rating_averages': rating_averages })

def CompanyReviews(request, post_id):
  company = get_object_or_404(Company, id=post_id)
  # user = request.user
  reviews = Review.objects.filter(company=company)

  context = { 'company': company, 'reviews': reviews}

  return render(request, 'reviews.html', context=context)

def CreateReview(request):
  if request.method == "POST":
    form = ReviewForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('index')
  else:
    form = ReviewForm()
  return render(request, 'create_review.html', {'form': form})

def AddCompany(request):
  if request.method == "POST":
    form = CompanyForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('company-detail', id=company.pk)
  else:
      form = CompanyForm()
  return render(request, 'add_company.html', { 'form': form})

class IndexListView(generic.ListView):
  model = Review
  
  def get_queryset(self):
    return Company.objects.annotate(avg_rating=Avg('reviews__rating'))

class ReviewDetailView(generic.DetailView):
  model = Review

class CompanyDetailView(generic.DetailView):
  model = Company          