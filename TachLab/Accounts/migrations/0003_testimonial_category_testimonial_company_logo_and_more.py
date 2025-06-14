# Generated by Django 5.2.2 on 2025-06-09 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_testimonialcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.testimonialcategory'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='company_logo',
            field=models.ImageField(blank=True, upload_to='testimonials/logos/'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='video_review_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
