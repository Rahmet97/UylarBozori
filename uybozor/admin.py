from django.contrib import admin
from .models import Announcement, Blog

for cls in (Announcement, Blog):
    admin.site.register(cls)
