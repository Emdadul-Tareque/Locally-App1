# Generated by Django 3.0.4 on 2020-03-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_app', '0002_blogpost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
