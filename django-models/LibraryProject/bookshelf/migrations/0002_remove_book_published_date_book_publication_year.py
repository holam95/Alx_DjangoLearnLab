# Generated by Django 4.2.16 on 2024-11-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(default=1949),
            preserve_default=False,
        ),
    ]
