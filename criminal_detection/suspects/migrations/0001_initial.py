# Generated by Django 5.0.7 on 2024-07-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suspect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('crime_incidents', models.TextField()),
                ('arrest_reason', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
