# Generated by Django 5.0.7 on 2024-10-04 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0016_billingstatus_billing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitiesavailed',
            name='customer_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activities_availed', to='transactions.billing'),
        ),
        migrations.AlterField(
            model_name='amenitiesavailed',
            name='customer_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='amenities_availed', to='transactions.billing'),
        ),
        migrations.AlterField(
            model_name='foodbill',
            name='customer_bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='food_bill', to='transactions.billing'),
        ),
    ]
