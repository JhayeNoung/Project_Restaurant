# Generated by Django 5.0.1 on 2024-02-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='description',
            new_name='menu_item_description',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
