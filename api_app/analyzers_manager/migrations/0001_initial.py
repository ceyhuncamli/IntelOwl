# Generated by Django 3.2.4 on 2021-06-22 10:25

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("api_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnalyzerReport",
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
                ("analyzer_name", models.CharField(max_length=128, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("running", "running"),
                            ("failed", "failed"),
                            ("success", "success"),
                        ],
                        max_length=50,
                    ),
                ),
                ("report", models.JSONField(default=dict)),
                (
                    "errors",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, default=list, max_length=512
                        ),
                        size=None,
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="analyzer_reports",
                        to="api_app.job",
                    ),
                ),
            ],
        ),
    ]
