# Generated by Django 3.0.4 on 2020-03-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_foods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parlor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('expert', models.TextField()),
                ('charge', models.CharField(max_length=20)),
            ],
        ),
    ]
