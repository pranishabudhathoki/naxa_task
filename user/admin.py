from django.contrib import admin

from .models import City, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(City)
