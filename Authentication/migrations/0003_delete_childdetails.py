# Generated by Django 3.2 on 2023-06-10 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_alter_childdetails_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChildDetails',
        ),
    ]
