# Generated by Django 4.2 on 2024-04-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_remove_blogs_uploade_on_blogs_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='picture',
            field=models.ImageField(upload_to='blogs/'),
        ),
    ]
