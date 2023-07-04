# Generated by Django 4.2.2 on 2023-06-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop_projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=30, unique=True)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
    ]