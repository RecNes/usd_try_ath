# Generated by Django 3.2.11 on 2022-01-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_time_high', '0008_auto_20220104_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='alltimehigh',
            name='last_notification_date',
            field=models.DateTimeField(null=True, verbose_name='Son Bildirim Zamanı'),
        ),
        migrations.AddField(
            model_name='oneunitdropped',
            name='last_notification_date',
            field=models.DateTimeField(null=True, verbose_name='Son Bildirim Zamanı'),
        ),
    ]
