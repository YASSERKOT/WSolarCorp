# Generated by Django 2.0.7 on 2018-07-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('high', models.DecimalField(decimal_places=2, max_digits=19)),
                ('width', models.DecimalField(decimal_places=2, max_digits=19)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
