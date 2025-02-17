# Generated by Django 5.0.3 on 2024-03-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
