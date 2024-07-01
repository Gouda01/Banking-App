from django.db import models
from shortuuid.django_fields import ShortUUIDField

from userauths.models import User
from account.models import Account

TRANSACTION_TYPE = (
    ("transfer", "Transfer"),
    ("recieved", "Recieved"),
    ("withdraw", "Withdraw"),
    ("refund", "Refund"),
    ("request", "Request"),
    ("none", "None"),
)

TRANSACTION_STATUS = (
    ("failed", "Failed"),
    ("completed", "Completed"),
    ("pending", "Pending"),
    ("processing", "Processing"),
    ("requested", "Requested"),
)


class Transaction (models.Model):
    transaction_id = ShortUUIDField(unique=True, length=15, max_length=20, prefix="TRN")
    user = models.ForeignKey(User, related_name="user", on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.CharField(max_length=500)

    reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.SET_NULL, null=True)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.SET_NULL, null=True)

    reciever_account = models.ForeignKey(Account, related_name="reciever_account", on_delete=models.SET_NULL, null=True)
    sender_account = models.ForeignKey(Account, related_name="sender_account", on_delete=models.SET_NULL, null=True)

    status = models.CharField(choices=TRANSACTION_STATUS, max_length=100, default="pending")
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=100, default="none")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        try:
            return f"{self.user}"
        except :
            return f"Transaction"
    