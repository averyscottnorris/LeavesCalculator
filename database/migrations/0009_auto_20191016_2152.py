# Generated by Django 2.2.6 on 2019-10-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20191016_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='perleav',
            name='perleav_pidm',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perleav',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
