# Generated by Django 4.0.4 on 2022-05-28 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0002_remove_category_category_name_remove_image_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]