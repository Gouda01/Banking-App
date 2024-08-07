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


@login_required
def AmountRequestProcess(request, account_number):
    account = Account.objects.get(account_number=account_number)

    sender = request.user
    reciever = account.user


    sender_account = request.user.account
    reciever_account = account

    if request.method == "POST":
        amount = request.POST.get('amount-request')
        description = request.POST.get('description')

        new_request = Transaction.objects.create(
            user = request.user,
            amount = amount,
            description = description,

            sender = sender,
            reciever = reciever,

            sender_account = sender_account,
            reciever_account = reciever_account,

            status = "request_processing",
            transaction_type = "request",

        )

        new_request.save()
        transaction_id = new_request.transaction_id
        messages.success(request,'Success Request money')
        return redirect('core:amount-request-confirmation', account.account_number, transaction_id)

    else :
        messages.warning(request,'Error Occured, Try again later.')
        return redirect('account:dashboard')


@login_required
def AmountRequestConfirmation(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account': account,
        'transaction': transaction,
    }
    
    return render(request, 'payment_request/amount-request-confirmation.html', context)


@login_required
def AmountRequestFinalProcess(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    if request.method == "POST":
        pin_number = request.POST.get("pin-number")
        if pin_number == request.user.account.pin_number :
            transaction.status = "request_sent"
            transaction.save()

            messages.success(request, 'Your payment request have been sent successfuly.')
            return redirect ('core:amount-request-completed', account.account_number, transaction.transaction_id)
    else:
        messages.warning(request, 'An Error Occured, try again later.')
        return redirect('account:dashboard')
    
@login_required
def RequestCompleted(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account': account,
        'transaction': transaction,
    }

    return render(request, 'payment_request/amount-request-complated.html', context)

    