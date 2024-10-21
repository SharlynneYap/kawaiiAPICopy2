# Generated by Django 5.1.1 on 2024-09-25 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_activitiesavailed_hours_availed'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='paymentFor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.paymentfor'),
        ),
    ]
