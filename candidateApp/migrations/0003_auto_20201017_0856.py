# Generated by Django 3.1.2 on 2020-10-17 08:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('candidateApp', '0002_auto_20201016_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidateId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
