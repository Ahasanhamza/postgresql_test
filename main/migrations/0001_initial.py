# Generated by Django 3.2.7 on 2021-09-12 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pigeons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pigeons_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('Bread_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pigeons')),
            ],
        ),
        migrations.CreateModel(
            name='Pigeons_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origine', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('pigeons_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pigeons')),
            ],
        ),
    ]
