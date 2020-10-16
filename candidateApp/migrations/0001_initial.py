# Generated by Django 3.1.2 on 2020-10-16 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pagesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidateId', models.UUIDField(default='0C85B9', editable=False, primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='', max_length=300)),
                ('email', models.EmailField(default='', max_length=50)),
                ('interestedRole', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagesApp.role')),
            ],
        ),
    ]