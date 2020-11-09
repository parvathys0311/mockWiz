# Generated by Django 3.1.2 on 2020-10-19 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagesApp', '0003_auto_20201019_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='functionName',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='role',
            name='roleFunction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pagesApp.function'),
        ),
    ]