# Generated by Django 4.2.6 on 2023-11-01 10:56

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_created_at_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 1, 10, 56, 39, 833723, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2023, 11, 1, 10, 56, 39, 834589, tzinfo=datetime.timezone.utc), verbose_name='last login'),
        ),
    ]
