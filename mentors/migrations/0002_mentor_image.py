# Generated by Django 3.2.7 on 2021-09-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='image',
            field=models.ImageField(default=True, upload_to='images/', verbose_name='Image'),
        ),
    ]