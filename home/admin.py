from django.contrib import admin
from .models import TODO, TimingTodo

# Register your models here.
admin.site.register(TODO)
admin.site.register(TimingTodo)
