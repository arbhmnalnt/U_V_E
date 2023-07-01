# Generated by Django 4.2.2 on 2023-06-25 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('number', models.SmallIntegerField(blank=True, null=True)),
                ('kind', models.CharField(blank=True, choices=[('P3', 'بلايستيشن 3'), ('P4', 'بلايستيشن 4')], default='P4', max_length=2, null=True)),
                ('place', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='مدة الحجز بالدقائق')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='play.device')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=75, null=True, verbose_name='الطلب')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='السعر')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='play.rent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]