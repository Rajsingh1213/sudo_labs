# Generated by Django 5.2.2 on 2025-07-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
