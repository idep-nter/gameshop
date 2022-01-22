# Generated by Django 4.0.1 on 2022-01-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField(max_length=5)),
                ('description', models.TextField(null=True)),
                ('category', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
            ],
        ),
    ]
