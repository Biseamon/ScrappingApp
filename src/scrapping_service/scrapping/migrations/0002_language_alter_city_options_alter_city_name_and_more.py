# Generated by Django 4.0.5 on 2022-08-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Programming language')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Programming language',
                'verbose_name_plural': 'Programming languages',
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Name of the location', 'verbose_name_plural': 'Name of the locations'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name of the location'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]