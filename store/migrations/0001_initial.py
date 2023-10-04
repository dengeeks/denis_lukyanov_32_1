# Generated by Django 4.2.5 on 2023-09-23 08:52

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='category_icon')),
                ('title', models.CharField(max_length=64)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='store_image')),
                ('title', models.CharField(max_length=64)),
                ('parameters', models.TextField()),
                ('description', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('price', models.FloatField()),
                ('category_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]