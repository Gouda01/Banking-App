from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import KYC, Account
from .forms import KYCForm

# Create your views here.

# @login_required
def account (request):
    if request.user.is_authenticated :
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, 'You need to submit your KYC')
            return redirect("account:kyc-reg")
        
        account = Account.objects.get(user=request.user)
    else :
        messages.warning(request, 'You need to Sign in to access the dashboard')
        return redirect("userauths:sign-in")
    

    context = {
        "kyc":kyc,
        "account":account,
    }
    return render(request,'account/account.html', context)

@login_required
def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None

    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Form submitted successfuly, In review now.")

            return redirect("core:index")
    else :
        form = KYCForm(instance=kyc)

    context = {
        "account": account,
        "kyc": kyc,
        "form": form,
    }
    return render(request, "account/kyc-form.html", context)


@login_required
def dashboard(request):
    if request.user.is_authenticated :
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, 'You need to submit your KYC')
            return redirect("account:kyc-reg")
        
        account = Account.objects.get(user=request.user)
    else :
        messages.warning(request, 'You need to Sign in to access the dashboard')
        return redirect("userauths:sign-in")
    

    context = {
        "kyc":kyc,
        "account":account,
    }
    
    return render(request, 'account/dashboard.html', context)