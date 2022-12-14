# Generated by Django 4.1 on 2022-09-07 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0004_alter_student_teachers_alter_user_role"),
        ("Quizzes", "0015_rename_quiz_response_quiz_alter_response_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="response",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Users.student"
            ),
        ),
    ]
