# Generated by Django 2.2.4 on 2019-09-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=6)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
