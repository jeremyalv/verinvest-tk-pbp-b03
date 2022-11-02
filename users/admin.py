from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import VerinvestUser

class VerinvestUserAdmin(UserAdmin):
    model = VerinvestUser

admin.site.register(VerinvestUser, VerinvestUserAdmin)
