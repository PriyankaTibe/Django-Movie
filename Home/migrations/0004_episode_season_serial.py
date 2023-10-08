# Generated by Django 3.2 on 2021-11-25 21:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_homepagemodel_page_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('Serial_name', models.CharField(max_length=200)),
                ('release_date', models.CharField(default='None', max_length=70)),
                ('short_intro', models.TextField(max_length=700)),
                ('IMDb_RATING', models.CharField(default=None, max_length=50)),
                ('poster', models.ImageField(upload_to='Posters/')),
                ('serie_page_poster', models.ImageField(blank=True, null=True, upload_to='Posters/SerialPage/')),
                ('summary', models.TextField(max_length=1600)),
                ('trailer', models.CharField(blank=True, max_length=650, null=True)),
                ('page_view', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('director', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.director')),
                ('genre', models.ManyToManyField(to='Home.Genre')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.serial')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.serial')),
            ],
        ),
    ]
