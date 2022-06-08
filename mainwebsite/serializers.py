# change data to json
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Company, Gallery, News, SendEmailUser


class GallerySerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
  
  class Meta:
    model = Gallery
    fields = ('id', 'title', 'image', 'content', 'created_at')

class NewsSerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M")
  
  class Meta:
    model = News
    fields = ('id', 'title', 'image', 'content', 'created_at')
    

class SendEmailUserSerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
  update_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
  
  class Meta:
    model = SendEmailUser
    fields = ('id', 'email', 'created_at', 'update_at')
    read_only_fields = ('created_at', 'updated_at')
    
class CompaniesSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Company
    fields = ('id', 'companyName', 'companyPostCode', 'companyAddress', 'companyPhoneNumber', 'companyFax')