from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import ReviewForm
from .models import Company, Review

# Create your views here.
def index(request):
  companies = Company.objects.all()
  return render(request, 'index.html', { 'companies': companies })

def CompanyDetails(request, post_id):
  company = get_object_or_404(Company, id=post_id)
  # user = request.user
  reviews = Review.objects.filter(company=company)

  context = { 'company': company, 'reviews': reviews}

  return render(request, 'details.html', context=context)

def CreateReview(request):
  if request.method == "POST":
    form = ReviewForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Post successfully created!")
        return redirect('review-detail', id=post_id)
  else:
    form = ReviewForm()
  return render(request, 'create_review.html', {'form': form})