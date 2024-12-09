from django.urls import path
from .views import CustomerDashboardView

urlpatterns = [
    path('dashboard/', CustomerDashboardView.as_view(), name='dashboard'),
]
