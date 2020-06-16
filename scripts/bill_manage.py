from datetime import timedelta,datetime

from django.utils import timezone

from user.models import Bill

def run():
    # Get all questions
    unpaid_bills = Bill.objects.filter(status='NOT PAID')
    # Delete questions
    for bill in unpaid_bills:
        if(timezone.now()-timedelta(seconds=3)>bill.generated_on)
               bill.update(bill.amount=bill.amount+10)