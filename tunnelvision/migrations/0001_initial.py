# Generated by Django 4.2.16 on 2024-10-14 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("symbol", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="MonitoringConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("recipientMail", models.EmailField(max_length=254)),
                ("senderMail", models.EmailField(max_length=254)),
                ("lower_bound", models.DecimalField(decimal_places=2, max_digits=10)),
                ("upper_bound", models.DecimalField(decimal_places=2, max_digits=10)),
                ("frequency", models.IntegerField()),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tunnelvision.asset",
                    ),
                ),
            ],
        ),
    ]
