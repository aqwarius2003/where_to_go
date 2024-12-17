# Generated by Django 4.2 on 2024-12-13 12:47

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['title'], 'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.RemoveField(
            model_name='place',
            name='description_long',
        ),
        migrations.RemoveField(
            model_name='place',
            name='description_short',
        ),
        migrations.AddField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Детальное описание'),
        ),
        migrations.AddField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='order',
            field=models.IntegerField(db_index=True, default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='places.place', verbose_name='Локация'),
        ),
    ]
