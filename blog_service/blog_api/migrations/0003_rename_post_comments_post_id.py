# Generated by Django 3.2.13 on 2022-04-22 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0002_auto_20220422_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='post',
            new_name='post_id',
        ),
    ]
