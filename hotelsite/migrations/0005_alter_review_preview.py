# Generated by Django 4.1.2 on 2022-11-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelsite', '0004_alter_review_options_remove_review_textbody_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='preview',
            field=models.TextField(max_length=155),
        ),
    ]