# Generated by Django 4.1 on 2022-09-06 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Quizzes", "0006_alter_quiz_organizer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quiz", old_name="Organizer", new_name="Organizer_id",
        ),
    ]
