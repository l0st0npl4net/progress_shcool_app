# Generated by Django 5.0.3 on 2024-05-17 22:08

import courses.image_load
import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceo_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='CEO тайтл')),
                ('ceo_description', models.TextField(blank=True, null=True, verbose_name='CEO описание')),
                ('title', models.CharField(max_length=150, null=True, unique=True, verbose_name='Название страницы')),
                ('path', models.CharField(choices=[('/', 'Home'), ('/about_us/', 'About Us'), ('/courses/', 'Courses'), ('/online_tests/all_tests/', 'Online Tests'), ('/lessons/', 'Lessons')], default='/', verbose_name='Путь до страницы')),
                ('text_primary', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Основной блок')),
                ('text_secondary', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Дополнительный блок')),
            ],
            options={
                'verbose_name': 'Тексты для страниц',
                'verbose_name_plural': 'Тексты для страниц',
            },
        ),
        migrations.CreateModel(
            name='CarouselSponsorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=courses.image_load.HomeUpload._upload, verbose_name='Изображение')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsors', to='pages.pagemodel', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Спонсоры',
                'verbose_name_plural': 'Спонсоры',
            },
        ),
        migrations.CreateModel(
            name='CarouselReviewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Имя')),
                ('review', models.TextField(verbose_name='Отзыв')),
                ('image', models.ImageField(upload_to=courses.image_load.HomeUpload._upload, verbose_name='Изображение')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pages.pagemodel', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='CarouselMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=courses.image_load.HomeUpload._upload, verbose_name='Изображение')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main', to='pages.pagemodel', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Главная карусель',
                'verbose_name_plural': 'Главная карусель',
            },
        ),
        migrations.CreateModel(
            name='CarouselAdvantagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Текст')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adv', to='pages.pagemodel', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Статичные блоки',
                'verbose_name_plural': 'Статичные блоки',
            },
        ),
    ]
