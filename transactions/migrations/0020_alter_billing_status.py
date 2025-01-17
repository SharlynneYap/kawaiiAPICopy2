# Generated by Django 5.0.7 on 2024-10-14 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0019_foodbill_date_foodbill_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="status",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="transactions.billingstatus",
            ),
        ),
    ]
