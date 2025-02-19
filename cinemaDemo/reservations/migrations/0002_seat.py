# Generated by Django 3.1.1 on 2020-10-10 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=3)),
                ('corMovie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movieSeats', to='reservations.movie')),
            ],
        ),
    ]
