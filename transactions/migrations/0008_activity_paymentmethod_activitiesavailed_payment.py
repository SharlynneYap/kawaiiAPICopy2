# Generated by Django 5.1.1 on 2024-09-11 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_alter_guestlist_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ActivitiesAvailed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.transaction')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.activity')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.transaction')),
                ('mop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.paymentmethod')),
            ],
        ),
    ]
