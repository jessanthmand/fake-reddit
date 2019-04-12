from django.contrib import admin

# Register your models here.

from .models import Comments, Posts

admin.site.register([Comments, Posts])