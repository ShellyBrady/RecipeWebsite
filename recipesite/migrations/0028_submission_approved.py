# Generated by Django 3.2.18 on 2023-06-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0027_rename_author_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
