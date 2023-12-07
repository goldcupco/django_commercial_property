from django.contrib import admin

# Register your models here.

# commercial_app/admin.py

from django.contrib import admin
from .models import CommercialProperty

admin.site.register(CommercialProperty)
