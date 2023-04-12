# Generated by Django 4.1.6 on 2023-04-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0003_delete_projects"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
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
                ("title", models.CharField(max_length=100)),
                ("body", models.TextField(default=None)),
                ("employee", models.CharField(max_length=100)),
                ("img", models.FilePathField(path="/static/statics/images/")),
                ("employee_img", models.FilePathField(path="/static/statics/images/")),
            ],
        ),
    ]