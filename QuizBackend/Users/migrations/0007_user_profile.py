# Generated by Django 4.1 on 2022-10-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0006_student_teachers"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile",
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
