# Generated by Django 5.1.2 on 2024-10-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FName', models.CharField(blank=True, max_length=100, null=True)),
                ('LName', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Messages', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]