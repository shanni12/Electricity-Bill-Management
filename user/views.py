from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Complaint, Bill
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core import serializers

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
import json
# Create your views here.
# bills = [{'id': 'shaja452',
#           'units': 20,
#           'amount': 100,
#           'month': 'April 2020'},
#          {'id': 'shaja452',
#           'units': 20,
#           'amount': 100,
#           'month': 'April 2020'},
#          {'units': 20,
#           'id': 'shaja452',
#           'amount': 100,
#           'month': 'April 2020'},
#          {'units': 20,
#           'id': 'shaja452',
#           'amount': 100,
#           'month': 'April 2020'}
#          ]


def register(request):
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })

@login_required
def home(request):
    if(request.method=="POST"):
        bills_objects=Bill.objects.filter(meter_id=request.POST.get('meter')).order_by('-generated_on')
        serialized_bills_data = json.loads(serializers.serialize('json', bills_objects))
        bills = [{"bill_id": serialized_bill_data['pk'], **serialized_bill_data['fields']} for serialized_bill_data in serialized_bills_data]
        print(bills)
        bills_js=[{"bill_id": serialized_bill_data['pk'], "status":serialized_bill_data['fields']['status']} for serialized_bill_data in serialized_bills_data]
        print(bills_js)
        return render(request,'user/home.html',{'bills':bills,'bills_js': bills_js})
        
    #bills = Bill.objects.order_by('-generated_on')

    #return render(request, 'user/home.html', {'bills': bills})
    return render(request,'user/meter.html')


@login_required
def view_complaints(request):
    print(request)
    complaints = Complaint.objects.filter(user=request.user)

    return render(request, 'user/view_complaint.html', {'complaints': complaints})


def about(request):
    return render(request, 'user/about.html')


@login_required
def complaint(request, bill_id):
    bill = get_object_or_404(Bill, bill_id=bill_id)
    print(bill)
    if(request.method == "POST"):
        print(request.POST)
        print(request.user)
        #bill = Bill.objects.get(id=bill_id)

        try:
            complaint = Complaint.objects.create(bill_id=bill, issue=request.POST.get(
                'issue', 'shakjnd ned'), meter_id=bill.meter_id,user=request.user)
            complaint.save()
            messages.success(request, f'Complaint raised Successfully!')
        except Exception as e:
            print(e)
        bills=Bill.objects.filter(meter_id=bill.meter_id).order_by('-generated_on')
       
        return render(request,'user/home.html',{'bills':bills})
    
        # form = ComplaintForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     bill_id = form.cleaned_data.get('bill_id')
        #     messages.success(request, f'Complaint created on {bill_id}!')
        #     return redirect('user-home')

    return render(request, 'user/complaint.html', {'bill_id': bill_id})


@login_required
def transaction(request, bill_id):
    bill_object = get_object_or_404(Bill, bill_id=bill_id)
    if(request.method == "POST"):
        print(request.POST.get('remarks'))
        myStr = datetime.now()
        print(request.POST.get('transaction_mode'))
        print(bill_id)
        Bill.objects.filter(bill_id=bill_id).update(
            status='PAID', payment_mode=request.POST.get('transaction_mode'), paid_on=myStr)
        messages.success(request, f'Bill Paid!')
        bills=Bill.objects.filter(meter_id=bill_object.meter_id).order_by('-generated_on')
        return render(request,'user/home.html',{'bills':bills})

    return render(request, 'user/transaction.html', {'bill_id': bill_id, 'bill_amount': bill_object.amount, 'bill_units': bill_object.units})


def handler404(request, exception):
    url_path = request.get_full_path()
    print(url_path)
    url_parts = url_path.strip('/').split('/')
    print(url_parts)
    if(len(url_parts) == 3):
        print('**')
        return render(request, 'user/404.html', {'bill_id': url_parts[2]}, status=404)
    else:
        return render(request, 'user/commonerrors.html')
