# Generated by Django 3.0.1 on 2022-02-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='full_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]