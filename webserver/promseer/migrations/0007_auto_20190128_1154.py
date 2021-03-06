# Generated by Django 2.1.5 on 2019-01-28 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promseer', '0006_auto_20190128_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='k',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='label',
            name='v',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='label',
            unique_together={('target', 'k', 'v')},
        ),
        migrations.AlterIndexTogether(
            name='label',
            index_together={('target', 'k', 'v')},
        ),
    ]
