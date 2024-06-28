# Generated by Django 4.2 on 2024-06-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_kyc_account_alter_kyc_identity_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_status',
            field=models.CharField(choices=[('in-active', 'In-active'), ('active', 'Active'), ('pending', 'Pending')], default='in-active', max_length=50),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=40),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='identity_type',
            field=models.CharField(choices=[('drivers_licence', 'Drivers Licence'), ('international_passport', 'International Passport'), ('national_id_card', 'National ID Card')], max_length=140),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='marrital_status',
            field=models.CharField(choices=[('other', 'Other'), ('single', 'Single'), ('married', 'Married')], max_length=40),
        ),
    ]