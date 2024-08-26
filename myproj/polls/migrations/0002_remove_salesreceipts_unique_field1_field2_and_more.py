# Generated by Django 4.2.15 on 2024-08-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='salesreceipts',
            name='unique_field1_field2',
        ),
        migrations.AddConstraint(
            model_name='salesreceipts',
            constraint=models.UniqueConstraint(fields=('transaction_id', 'transaction_date', 'transaction_time', 'sales_outlet', 'product'), name='unique_field1_field2'),
        ),
    ]
