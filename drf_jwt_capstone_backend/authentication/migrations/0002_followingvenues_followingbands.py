# Generated by Django 4.0b1 on 2021-11-08 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowingVenues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
                ('venue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.venue')),
            ],
        ),
        migrations.CreateModel(
            name='FollowingBands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.band')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]
