# Generated by Django 4.2 on 2024-06-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_kyc_gender_alter_kyc_identity_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='identity_type',
            field=models.CharField(choices=[('international_passport', 'International Passport'), ('national_id_card', 'National ID Card'), ('drivers_licence', 'Drivers Licence')], max_length=140),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='marrital_status',
            field=models.CharField(choices=[('other', 'Other'), ('single', 'Single'), ('married', 'Married')], max_length=40),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
    ]
