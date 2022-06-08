from django.contrib import admin
from .models import Company, Gallery, News, SendEmailUser

# Register your models here.
admin.site.register(Gallery)
admin.site.register(News)
admin.site.register(SendEmailUser)
admin.site.register(Company)

