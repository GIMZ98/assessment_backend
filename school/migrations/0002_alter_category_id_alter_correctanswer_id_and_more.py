# Generated by Django 4.0.5 on 2024-03-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(max_length=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='correctanswer',
            name='id',
            field=models.CharField(max_length=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='summary',
            name='sydney_participant',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='sydney_percentile',
            field=models.IntegerField(),
        ),
    ]
