from django.contrib import admin
from user.models import Bill,Complaint,Meter,House
from django.contrib.auth.models import User
# Register your models here.
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    
    readonly_fields = ['paid_on', 'remarks','bill_id','status','payment_mode']

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    
    readonly_fields = [ 'issue','bill_id']
admin.site.register(House)
admin.site.register(Meter)