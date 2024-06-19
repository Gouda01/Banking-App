from django.shortcuts import render, redirect
from django.contrib import messages

from .models import KYC, Account
from .forms import KYCForm

# Create your views here.

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