# Generated by Django 3.0.4 on 2020-03-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('food_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('quantity', models.CharField(max_length=50)),
            ],
        ),
    ]
