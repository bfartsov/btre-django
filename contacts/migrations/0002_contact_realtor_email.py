# Generated by Django 3.1.2 on 2020-10-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='realtor_email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
