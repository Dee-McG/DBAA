# Generated by Django 4.0.5 on 2022-06-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_eventnumbers_event_commentevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fee',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
