# Generated by Django 4.1.2 on 2022-11-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelsite', '0014_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
