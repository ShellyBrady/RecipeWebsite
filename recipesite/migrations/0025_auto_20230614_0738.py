# Generated by Django 3.2.18 on 2023-06-14 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0024_auto_20230613_1226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-created_on']},
        ),
    ]
