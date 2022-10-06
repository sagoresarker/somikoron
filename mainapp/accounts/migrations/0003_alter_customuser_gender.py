# Generated by Django 4.1.2 on 2022-10-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Prefer Not to Say')]),
        ),
    ]
