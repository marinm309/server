# Generated by Django 5.0.7 on 2024-08-10 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_appuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
