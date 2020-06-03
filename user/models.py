from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import uuid
# Create your models here.


class Bill(models.Model):

    bill_status_choices = [
        ('PAID', 'PAID'),
        ('NOT PAID', 'NOT PAID')
    ]

    bill_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.IntegerField()
    amount = models.IntegerField()
    generated_on = models.DateField(auto_now_add=True,editable=True)
    paid_on = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=bill_status_choices, default='NOT PAID')
    payment_mode = models.CharField(max_length=300, blank=True, null=True,editable=False)


class TransactionModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bill_id = models.OneToOneField(Bill, on_delete=models.CASCADE, null=True)
    payment_choices = [
        ('CREDIT CARD', 'CREDIT CARD'),
        ('DEBIT CARD', 'DEBIT CARD'),
        ('UPI', 'UPI')
    ]
    mode = models.CharField(max_length=100, choices=payment_choices)


class Complaint(models.Model):
    complaint_status_choices = [
        ('RESOLVED', 'RESOLVED'),
        ('NOT RESOLVED', 'NOT RESOLVED')
    ]
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    issue = models.CharField(max_length=300)
    status = models.CharField(
        max_length=100, choices=complaint_status_choices, default='NOT RESOLVED')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
