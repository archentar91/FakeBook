# Generated by Django 4.2.3 on 2023-07-29 23:32

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]