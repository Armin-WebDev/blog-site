# Generated by Django 3.2.4 on 2022-09-18 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_article_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='cover',
        ),
    ]
