# Generated by Django 3.2.8 on 2022-03-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
