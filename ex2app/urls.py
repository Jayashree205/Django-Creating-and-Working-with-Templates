from django.urls import path
from . import views

urlpatterns = [
    path('oddfilter/', views.oddfilter, name='oddfilter'),  # Maps /oddfilter/ URL to the combined oddfilter view
]
