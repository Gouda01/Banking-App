# Generated by Django 4.2 on 2024-06-19 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='red_code',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh1234567890', length=10, max_length=20, prefix='', unique=True),
        ),
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=1000)),
                ('image', models.ImageField(default='default.jpg', upload_to='kyc')),
                ('marrital_status', models.CharField(choices=[('other', 'Other'), ('married', 'Married'), ('single', 'Single')], max_length=40)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=40)),
                ('identity_type', models.CharField(choices=[('international_passport', 'International Passport'), ('national_id_card', 'National ID Card'), ('drivers_licence', 'Drivers Licence')], max_length=140)),
                ('date_of_birth', models.DateField()),
                ('signature', models.ImageField(upload_to='kyc')),
                ('country', models.CharField(max_length=100)),
                ('stat', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=1000)),
                ('fax', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
