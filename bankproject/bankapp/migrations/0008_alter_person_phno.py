# Generated by Django 4.2.7 on 2024-02-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0007_alter_branch_options_alter_district_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phno',
            field=models.IntegerField(),
        ),
    ]