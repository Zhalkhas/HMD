# Generated by Django 2.1.8 on 2019-06-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190603_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='allergia',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3),
        ),
    ]