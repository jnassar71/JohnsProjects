# Generated by Django 3.0.4 on 2020-06-08 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MiniCaseApp', '0002_auto_20200608_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseName', models.CharField(max_length=100)),
                ('CaseDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('ContractNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('DateCreated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContractDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=100)),
                ('ContractID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='MiniCaseApp.Contract', verbose_name='Contract')),
            ],
        ),
    ]