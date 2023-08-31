# Generated by Django 4.1.3 on 2023-08-28 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resim",
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
                ("resim", models.FileField(blank=True, upload_to="images/")),
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Urun",
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
                ("urun_adi", models.CharField(max_length=50)),
                ("urun_adedi", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "resim",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.resim"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fatura",
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
                ("fiyat", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "urun",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.urun"
                    ),
                ),
            ],
        ),
    ]
