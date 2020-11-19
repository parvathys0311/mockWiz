# Generated by Django 3.1.3 on 2020-11-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expertApp', '0007_auto_20201117_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='expertise',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='expert',
            name='published',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
    ]
