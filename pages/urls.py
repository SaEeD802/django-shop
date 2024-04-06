from django.urls import path
from .views import home_page

urlpatterns = [
    path('', home_page.as_view(), name='home'),
]