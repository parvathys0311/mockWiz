# Generated by Django 3.1.3 on 2020-11-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expertApp', '0006_expert_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='summary',
            field=models.TextField(blank=True, default=''),
        ),
    ]