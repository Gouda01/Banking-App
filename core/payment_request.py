from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal

from account.models import Account
from .models import Transaction

@login_required
def SearchUsersRequest(request):
    accounts = Account.objects.all()
    query = request.POST.get("account_number")
    
    if query :
        accounts = accounts.filter(
            Q(account_number=query)|
            Q(account_id=query)
        ).distinct()
        
    context = {
        'accounts':accounts,
        'query':query,
    }
    return render(request, 'payment_request/search-users.html', context)

@login_required
def AmoundRequest(request, account_number):
    account = Account.objects.get(account_number=account_number)
    
    context = {
        'account':account,
    }
    
    return render(request, 'payment_request/amount-request.html', context)

