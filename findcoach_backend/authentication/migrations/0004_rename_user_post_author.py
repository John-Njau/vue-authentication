# Generated by Django 4.1.3 on 2022-11-11 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_post"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="user",
            new_name="author",
        ),
    ]