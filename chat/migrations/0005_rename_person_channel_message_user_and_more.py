# Generated by Django 4.0.5 on 2022-09-02 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_rename_channel_people_channel_person_channel_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel_message',
            old_name='person',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='channel_person',
            old_name='person',
            new_name='user',
        ),
        migrations.AddField(
            model_name='channel',
            name='name',
            field=models.TextField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
