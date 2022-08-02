from django.contrib import admin

# Register your models here.
from .models import Note,Login

admin.site.register(Note)
admin.site.register(Login)