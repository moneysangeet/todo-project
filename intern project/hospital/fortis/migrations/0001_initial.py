# Generated by Django 5.0 on 2024-01-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('My_Image', models.ImageField(blank=True, null=True, upload_to='savedImages')),
            ],
        ),
    ]
