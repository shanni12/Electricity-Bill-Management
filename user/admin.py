from django.contrib import admin
from user.models import Bill,Complaint
from django.contrib.auth.models import User
# Register your models here.
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    
    readonly_fields = ['paid_on', 'remarks','bill_id','status']

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    
    readonly_fields = ['user', 'issue','bill_id']