# Generated by Django 4.1 on 2022-10-08 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0005_remove_student_teachers_room"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="Teachers",
            field=models.ManyToManyField(to="Users.teacher"),
        ),
    ]
