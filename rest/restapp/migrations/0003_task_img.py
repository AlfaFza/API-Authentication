# Generated by Django 3.2.9 on 2021-11-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image'),
        ),
    ]
