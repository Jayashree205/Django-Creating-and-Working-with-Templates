from django.contrib import admin
from django.urls import path
from ex2app import views as ex2app_views
from myapp import views as myapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ex2app_views.home, name='home'),  # Route for the home page
    path('oddfilter/', ex2app_views.oddfilter, name='oddfilter'),  # Combined odd/even and filter view
    path('about/', myapp_views.about, name='about'),  # Route for the About page
    path('home/', myapp_views.home, name='home_page'),  # Route for the Home page in myapp
]