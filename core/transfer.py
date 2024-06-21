from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from account.models import Account


@login_required
def search_users_account_number(request):

    accounts = Account.objects.all()

    context = {
        'accounts' : accounts,
    }

    return render (request, 'transfer/search-user-by-account-number.html', context)
