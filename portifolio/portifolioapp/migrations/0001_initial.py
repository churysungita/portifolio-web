# Generated by Django 4.0.2 on 2022-04-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
                ('link', models.URLField(max_length=50)),
            ],
        ),
    ]
