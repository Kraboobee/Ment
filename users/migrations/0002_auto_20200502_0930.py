# Generated by Django 3.0.5 on 2020-05-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accompaniment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='accompaniment',
            name='tel_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='accompaniment',
            name='tel_no2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='accompaniment',
            name='tel_no3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
