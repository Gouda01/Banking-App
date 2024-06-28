from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from account.models import Account


@login_required
def search_users_account_number(request):

    accounts = Account.objects.all()
    query = request.POST.get("account_number")

    if query :
        accounts = Account.objects.filter(
            Q(account_number=query)|
            Q(account_id=query)
        )

    context = {
        'accounts' : accounts,
        'query' : query,
    }

    return render (request, 'transfer/search-user-by-account-number.html', context)


@login_required
def AmountTransfer(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        account= None
        messages.warning(request, 'Account does not exist.')
        return redirect('core:search-account')

    context = {
        'account': account
    }
    return render(request, "transfer/amount-transfer.html", context)