# Generated by Django 3.1.7 on 2021-03-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_slider_button_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='button_link',
            field=models.URLField(default='https://www.youtube.com/channel/UCBJycsmduvYEL83R_U4JriQ'),
        ),
    ]
