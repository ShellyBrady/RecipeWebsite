# Generated by Django 3.2.18 on 2023-07-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0051_remove_recipe_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='username',
            new_name='username_id',
        ),
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
