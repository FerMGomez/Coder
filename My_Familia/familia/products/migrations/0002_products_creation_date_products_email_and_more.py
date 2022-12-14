# Generated by Django 4.1 on 2022-08-13 03:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="creation_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="products",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="altura",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="edad",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="sexo",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
