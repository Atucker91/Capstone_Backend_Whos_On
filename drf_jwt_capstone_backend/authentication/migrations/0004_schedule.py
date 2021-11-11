# Generated by Django 4.0b1 on 2021-11-11 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_user_postal_code_remove_venue_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('band_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.band')),
                ('venue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.venue')),
            ],
        ),
    ]