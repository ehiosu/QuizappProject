# Generated by Django 4.1 on 2022-09-06 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "Quizzes",
            "0010_rename_quiz_name_quiz_name_remove_quiz_organizer_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="Quiz",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="Quizzes.quiz",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="image1",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="image2",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="image3",
            field=models.URLField(blank=True, null=True),
        ),
    ]