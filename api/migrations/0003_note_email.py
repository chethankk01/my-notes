# Generated by Django 4.0.3 on 2022-05-16 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
