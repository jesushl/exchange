# Generated by Django 3.1.3 on 2020-11-08 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BM', 'Banco de Mexico'), ('FR', 'Fixer'), ('DO', 'Diario Oficial de la Federacion')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('date_from_source', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvesting.exchangesource')),
            ],
        ),
    ]
