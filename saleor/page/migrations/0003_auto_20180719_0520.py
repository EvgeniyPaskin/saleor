# Generated by Django 2.0.3 on 2018-07-19 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("page", "0002_auto_20180321_0417")]

    operations = [
        migrations.AlterModelOptions(
            name="page",
            options={
                "ordering": ("slug",),
                "permissions": (("manage_pages", "Manage pages."),),
            },
        )
    ]