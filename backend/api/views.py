# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, TravelHistory
from .serializers import UserProfileSerializer, TravelHistorySerializer
from .views import UserProfileDetail, TravelHistoryList


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class TravelHistoryList(generics.ListCreateAPIView):
    queryset = TravelHistory.objects.all()
    serializer_class = TravelHistorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
