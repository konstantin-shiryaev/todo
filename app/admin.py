from django.contrib import admin

# Register your models here.
from .models import Todo, Person

admin.site.register(Todo)
admin.site.register(Person)