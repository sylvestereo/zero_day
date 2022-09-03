# Generated by Django 4.1 on 2022-09-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=300, unique=True)),
                ("title", models.CharField(max_length=300, unique=True)),
                ("body", models.TextField(blank=True)),
                ("address", models.CharField(max_length=300, unique=True)),
                ("phone", models.IntegerField()),
                ("state", models.CharField(max_length=55, unique=True)),
                ("image_url", models.URLField(max_length=300, unique=True)),
            ],
        ),
    ]
