# Generated by Django 5.0.2 on 2024-03-02 07:35

import courses.image_load
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_image',
            field=models.ImageField(blank=True, null=True, upload_to=courses.image_load.AnswerUpload._upload),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to=courses.image_load.QuestionUpload._upload),
        ),
    ]