# Generated by Django 4.1.6 on 2023-02-27 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_remove_report_author_alter_report_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='price',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
