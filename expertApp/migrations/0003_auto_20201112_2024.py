# Generated by Django 3.1.3 on 2020-11-12 20:24

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('expertApp', '0002_auto_20201110_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='imageProfile',
            field=models.ImageField(default='./mockWizProject/static/images/default.png', upload_to='expert/profilePicture'),
        ),
        migrations.AddField(
            model_name='expert',
            name='jobTitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='expert',
            name='organization',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='expert',
            name='phoneNumber',
            field=phone_field.models.PhoneField(default='', help_text='Contact phone number', max_length=31),
        ),
    ]