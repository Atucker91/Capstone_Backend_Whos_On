# Generated by Django 4.0b1 on 2021-11-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='about',
            field=models.CharField(default=' ', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='img',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='about',
            field=models.CharField(default=' ', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='img',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
