# Generated by Django 4.2.1 on 2023-05-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=100)),
                ('matn', models.TextField()),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
                ('sana', models.DateField()),
            ],
        ),
    ]
