# Generated by Django 4.0.3 on 2022-03-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullurl', models.URLField()),
                ('title', models.TextField()),
                ('summary', models.TextField()),
                ('full_text', models.TextField()),
            ],
        ),
    ]
