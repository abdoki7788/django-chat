# Generated by Django 4.1.3 on 2022-11-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="slug",
            field=models.SlugField(null=True),
        ),
    ]