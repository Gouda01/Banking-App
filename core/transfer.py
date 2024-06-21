from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
