# Generated by Django 3.2.5 on 2022-05-03 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='brief_concent',
            new_name='brief_content',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='concent',
            new_name='content',
        ),
    ]
