from django.contrib import admin
from .models import Item, Place, Directory, DateRange, AccessionNumber

admin.site.register([Item, Place, Directory, DateRange, AccessionNumber])