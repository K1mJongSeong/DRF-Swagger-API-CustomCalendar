# Generated by Django 4.1.6 on 2023-03-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_image_alter_aprilback_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='nansu',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
