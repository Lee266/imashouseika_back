from abc import update_abstractmethods
from distutils.command.upload import upload
from email.mime import image
from http import server
from importlib.util import module_from_spec
from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.
class Gallery(models.Model):
  title = models.CharField('タイトル', max_length=50)
  image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
  content = models.TextField('本文')
  created_at = models.DateTimeField('作成日', auto_now_add=True)
  
  def __str__(self):
      return self.title

class News(models.Model):
  title = models.CharField('タイトル', max_length=50)
  image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
  content = models.TextField('お知らせの詳細')
  created_at = models.DateTimeField('作成日', auto_now_add=True)
  
  def __str__(self):
     return self.title

class SendEmailUser(models.Model):
  email = models.EmailField('email')
  created_at = models.DateTimeField('作成日', auto_now_add=True)
  update_at = models.DateTimeField('更新日', auto_now_add=True)
  
  def __str__(self):
     return self.email


class Company(models.Model):
  companyName = models.CharField('店舗名', max_length=100)
  companyPostCode = models.CharField('郵便番号', max_length=11)
  companyAddress = models.CharField('住所', max_length=300)
  companyPhoneNumber = models.CharField('電話番号', max_length=54)
  companyFax = models.CharField('FAX', null=True, blank=True, max_length=54)
  created_at = models.DateTimeField('作成日', auto_now_add=True)
  update_at = models.DateTimeField('更新日', auto_now_add=True)
  
  def __str__(self):
     return self.companyName

  
  
  
