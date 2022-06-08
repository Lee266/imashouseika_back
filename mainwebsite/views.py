from rest_framework import generics, viewsets
from .serializers import CompaniesSerializer, GallerySerializer, NewsSerializer, SendEmailUserSerializer
from .models import Company, Gallery, News, SendEmailUser
from mainwebsite import serializers

class GalleryView(generics.ListAPIView):
  queryset = Gallery.objects.all()
  serializer_class = GallerySerializer

class GalleryDetailView(generics.RetrieveAPIView):
  queryset = Gallery.objects.all()
  serializer_class = GallerySerializer

class NewsView(viewsets.ModelViewSet):
  queryset = News.objects.all()
  serializer_class = NewsSerializer

class NewsDetailView(generics.RetrieveAPIView):
  queryset = News.objects.all()
  serializer_class = NewsSerializer
  

class SendEmailUsersView(generics.ListCreateAPIView):
  queryset = SendEmailUser.objects.all()
  serializer_class = SendEmailUserSerializer

class SendEmailUsersDetailView(generics.RetrieveAPIView):
  queryset = SendEmailUser.objects.all()
  serializer_class = SendEmailUserSerializer

class CompaniesView(generics.ListAPIView):
  queryset = Company.objects.all()
  serializer_class = CompaniesSerializer

class CompaniesDetailView(generics.RetrieveAPIView):
  queryset = Company.objects.all()
  serializer_class = CompaniesSerializer
