# Generated by Django 4.2.7 on 2024-02-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='wikilink',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
