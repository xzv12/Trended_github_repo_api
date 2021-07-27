




from django.urls import path
from .views import fetch_trend_repos 

urlpatterns = [
    path('',fetch_trend_repos ,name='fetch_trend_repos'),

]
