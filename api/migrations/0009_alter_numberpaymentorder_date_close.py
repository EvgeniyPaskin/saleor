# Generated by Django 3.2.8 on 2021-10-26 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_numberpaymentorder_date_close'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberpaymentorder',
            name='date_close',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 26, 12, 12, 31, 806949), null=True, verbose_name='Когда закончить проверку оплаты'),
        ),
    ]