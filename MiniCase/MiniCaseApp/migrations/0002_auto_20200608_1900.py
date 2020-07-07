# Generated by Django 3.0.4 on 2020-06-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniCaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Address',
            field=models.CharField(default='N/A', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='City',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='State',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='Zip',
            field=models.CharField(default='N/A', max_length=20),
            preserve_default=False,
        ),
    ]