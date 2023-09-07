# Generated by Django 4.0.8 on 2023-09-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория(ю)', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Статья(ю)', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='view',
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
