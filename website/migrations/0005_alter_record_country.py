# Generated by Django 4.2.3 on 2023-07-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_record_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='country',
            field=models.CharField(max_length=50),
        ),
    ]
