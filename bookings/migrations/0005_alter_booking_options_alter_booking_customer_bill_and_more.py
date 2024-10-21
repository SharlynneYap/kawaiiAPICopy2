# Generated by Django 5.1.1 on 2024-10-02 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_rename_transaction_booking_customer_bill'),
        ('transactions', '0016_billingstatus_billing_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['check_in']},
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='transactions.billing'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='bookings.room'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='bookings.roomtype'),
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('room', 'check_in', 'check_out')},
        ),
    ]