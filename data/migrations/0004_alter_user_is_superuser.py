# Generated by Django 4.0.3 on 2022-04-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
