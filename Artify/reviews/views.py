from django.shortcuts import render, redirect
# from .forms import ReviewForm
from .models import Review

def leave_review(request, order_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user
            review.order_id = order_id
            review.save()
            return redirect('dashboard')
    else:
        form = ReviewForm()
    return render(request, 'reviews/leave_review.html', {'form': form})

