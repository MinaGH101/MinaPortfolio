# Generated by Django 4.1.6 on 2023-04-12 04:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_alter_projects_employee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Messages",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Example: +9121234567",
                                regex="^\\+?98?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("message", models.TextField()),
            ],
        ),
    ]