# Generated by Django 3.2.11 on 2023-01-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publis', '0014_auto_20230108_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='volume',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
