# Generated by Django 4.1 on 2022-09-05 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0002_alter_base_user_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="Registered_Teachers",
            field=models.ManyToManyField(blank=True, to="Users.teacher"),
        ),
    ]