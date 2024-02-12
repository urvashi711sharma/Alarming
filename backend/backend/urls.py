# api/urls.py
from django.urls import path
from api.views import UserProfileDetail, TravelHistoryList


urlpatterns = [
    path('user-profile/', UserProfileDetail.as_view()),
    path('travel-history/', TravelHistoryList.as_view()),
]
