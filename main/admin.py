from django.contrib import admin

from .models import Pigeons
from .models import Pigeons_Info
from .models import Pigeons_Status

admin.site.register(Pigeons)
admin.site.register(Pigeons_Info)
admin.site.register(Pigeons_Status)

