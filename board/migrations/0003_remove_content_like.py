# Generated by Django 3.2.5 on 2021-07-19 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20210719_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='like',
        ),
    ]