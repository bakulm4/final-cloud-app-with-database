# Generated by Django 3.1.3 on 2023-01-26 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230126_0631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='grade',
            new_name='question_text',
        ),
    ]
