# Generated by Django 5.0.2 on 2024-03-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_comment_options_alter_comment_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('user', 'User')], default=('user', 'User'), max_length=30, verbose_name='Должность'),
        ),
    ]