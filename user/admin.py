from django.contrib import admin
from user.models import Bill,Complaint
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Bill)
admin.site.register(Complaint)