from django.contrib import admin
from .models import Book, Instance, Lang


# Register your models here.

admin.site.register(Book)
admin.site.register(Instance)
admin.site.register(Lang)

