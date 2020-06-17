from datetime import timedelta,datetime

from django.utils import timezone

from user.models import Bill

def run():
    # Get all questions
    unpaid_bills = Bill.objects.filter(status='NOT PAID')
    # Delete questions
    for bill in unpaid_bills:
        print(bill.generated_on)
        print((datetime.now().date()-bill.generated_on).days)
        if(datetime.now().date()-timedelta(days=1)>bill.generated_on):
            bill.amount = bill.amount + 10*((datetime.now().date()-bill.generated_on).days)
        bill.save()
        #bill.update(amount=bill.amount+10)