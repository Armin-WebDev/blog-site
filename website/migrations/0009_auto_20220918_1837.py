# Generated by Django 3.2.4 on 2022-09-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_article_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.ImageField(default='covers/sample-image.jpg', upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatars/default.jpg', upload_to='avatars/'),
        ),
    ]