from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, ProfileSerializer, PeriodRecordSerializer
from .models import Profile, PeriodRecord

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class PeriodRecordViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PeriodRecord.objects.filter(profile=self.request.user.profile).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)
