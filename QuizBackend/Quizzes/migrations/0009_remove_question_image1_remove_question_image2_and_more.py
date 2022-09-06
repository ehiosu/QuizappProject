# Generated by Django 4.1 on 2022-09-06 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Quizzes", "0008_alter_question_quiz_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="question", name="Image1",),
        migrations.RemoveField(model_name="question", name="Image2",),
        migrations.RemoveField(model_name="question", name="Image3",),
        migrations.RemoveField(model_name="question", name="quiz_id",),
        migrations.AddField(
            model_name="question",
            name="Quiz",
            field=models.ForeignKey(
                default="15",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="question",
            field=models.TextField(max_length=500),
        ),
        migrations.AddField(
            model_name="question", name="image1", field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="question", name="image2", field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="question", name="image3", field=models.URLField(null=True),
        ),
    ]
