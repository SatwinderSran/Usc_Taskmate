# Generated by Django 3.0.4 on 2020-03-15 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortageReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly', models.CharField(max_length=50)),
                ('shortage_file', models.FileField(blank=True, upload_to='Shortage')),
                ('comment', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=False)),
                ('manage', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly', models.CharField(max_length=50)),
                ('quote_file', models.FileField(blank=True, upload_to='Quote')),
                ('comment', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=False)),
                ('manage', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Packing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packing_no', models.CharField(max_length=120)),
                ('packing_file', models.FileField(blank=True, upload_to='Packing')),
                ('comment', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=False)),
                ('manage', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly', models.CharField(max_length=12, unique=True)),
                ('mvl_No', models.CharField(blank=True, max_length=12, unique=True)),
                ('qty', models.PositiveIntegerField(unique=True)),
                ('fab_date', models.CharField(max_length=10, unique=True)),
                ('comments', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('requestor', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, default='default1.png', upload_to='boards')),
                ('image1', models.ImageField(blank=True, default='default1.png', upload_to='boards')),
                ('image2', models.ImageField(blank=True, default='default1.png', upload_to='boards')),
                ('image3', models.ImageField(blank=True, default='default1.png', upload_to='boards')),
                ('delivery', models.CharField(blank=True, max_length=20)),
                ('status', models.TextField(blank=True)),
                ('done', models.BooleanField(default=False)),
                ('manage', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'assembly',
                'verbose_name_plural': 'assemblies',
                'db_table': 'Assembly',
                'ordering': ['-date_posted'],
            },
        ),
    ]
