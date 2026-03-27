from django.contrib import admin
from .models import ConfirmCode
from django.contrib.auth.models import User

admin.site.register(ConfirmCode)

