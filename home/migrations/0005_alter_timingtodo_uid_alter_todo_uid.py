# Generated by Django 4.1.5 on 2023-01-28 14:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_todo_user_alter_timingtodo_uid_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('9ccac178-020d-4d7f-9ac1-adefb77fc5de'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('9ccac178-020d-4d7f-9ac1-adefb77fc5de'), editable=False, primary_key=True, serialize=False),
        ),
    ]
