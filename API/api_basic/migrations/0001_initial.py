# Generated by Django 3.0.5 on 2020-04-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=100)),
                ('memoryverse', models.TextField()),
                ('writing', models.TextField()),
                ('month', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
            ],
        ),
    ]
